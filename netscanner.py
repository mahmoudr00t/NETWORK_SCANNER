import scapy.all as scapy
import optparse
import os
import ipaddress


def check_root():
    if os.geteuid() != 0:
        print("[-] Please run this program with sudo.")
        print("Example: sudo python3 network_scanner.py -r 192.168.1.1/24")
        exit()


def validate_network(network_ip):
    try:
        ipaddress.ip_network(network_ip, strict=False)
        return True
    except ValueError:
        return False


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option(
        "-r",
        "--range",
        dest="network_ip",
        help="Device IP or network range"
    )

    parser.add_option(
        "-t",
        "--timeout",
        dest="timeout",
        default=1,
        help="Time to wait for responses"
    )

    options, arguments = parser.parse_args()

    if not options.network_ip:
        parser.error("[-] Please specify an IP address or range. Use -h for help.")

    if not validate_network(options.network_ip):
        parser.error("[-] Invalid IP address or network range. Example: 192.168.1.1/24")

    try:
        options.timeout = int(options.timeout)
    except ValueError:
        parser.error("[-] Timeout must be a number.")

    return options


def scan(network_ip, timeout):
    arp_request = scapy.ARP(pdst=network_ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = arp_broadcast / arp_request

    answered = scapy.srp(
        arp_request_broadcast,
        timeout=timeout,
        verbose=False
    )[0]

    client_list = []

    for ans in answered:
        client_dict = {
            "ip": ans[1].psrc,
            "mac": ans[1].hwsrc
        }
        client_list.append(client_dict)

    client_list.sort(key=lambda client: ipaddress.ip_address(client["ip"]))

    return client_list


def display_clients(clients):
    if not clients:
        print("[-] No devices found.")
        return

    print("{:<16} {}".format("IP Address", "MAC Address"))
    print("-" * 35)

    for client in clients:
        print("{:<16} {}".format(client["ip"], client["mac"]))


check_root()
options = get_arguments()
client_list = scan(options.network_ip, options.timeout)
display_clients(client_list)