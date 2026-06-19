# NETWORK_SCANNER
A Python-based ARP network scanner that discovers active devices on a local network and displays their IP and MAC addresses. The project uses Scapy for packet crafting and transmission, making it a practical introduction to network enumeration and cybersecurity fundamentals.

## Features

* Discover active hosts on a local network
* Display IP and MAC addresses of detected devices
* ARP-based host discovery
* Command-line argument support
* Network range validation
* Custom scan timeout option
* Sorted output for easier readability
* Clear error handling and user feedback

## Technologies Used

* Python 3
* Scapy
* Optparse
* ARP Protocol
* Ethernet Frames

## Requirements

* Linux Operating System
* Python 3
* Root privileges (sudo)
* Scapy

Install Scapy:

```bash
pip install scapy
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/network-scanner.git
cd network-scanner
```

## Usage

Basic scan:

```bash
sudo python3 network_scanner.py -r 192.168.1.1/24
```

Specify a custom timeout:

```bash
sudo python3 network_scanner.py -r 192.168.1.1/24 -t 3
```

## Arguments

| Argument | Description                        |
| -------- | ---------------------------------- |
| `-r`     | Target IP address or network range |
| `-t`     | Timeout in seconds (optional)      |

## Examples

Scan an entire subnet:

```bash
sudo python3 network_scanner.py -r 192.168.1.0/24
```

Wait longer for responses:

```bash
sudo python3 network_scanner.py -r 192.168.1.0/24 -t 5
```

## Sample Output

```text
IP Address       MAC Address
-----------------------------------
192.168.1.1      aa:bb:cc:dd:ee:ff
192.168.1.5      11:22:33:44:55:66
192.168.1.12     77:88:99:aa:bb:cc
```

## How It Works

1. The scanner creates an ARP request targeting the specified IP range.
2. The ARP request is encapsulated inside an Ethernet broadcast frame.
3. The broadcast is sent to all devices on the local network.
4. Devices that receive the request respond with their MAC address.
5. The scanner collects and displays the discovered hosts.

## Learning Objectives

This project was built to gain hands-on experience with:

* Network Enumeration
* ARP Protocol
* Packet Crafting
* Python Automation
* Scapy
* Linux Networking
* Command-Line Interface Development

## Educational Purpose

This project was developed as part of my cybersecurity learning journey. It is intended for educational purposes and authorized network testing only.

## Disclaimer

Only use this tool on networks you own or have explicit permission to assess. Unauthorized scanning of networks may violate laws, regulations, or organizational policies.

## Author

Mahmoud Ediem

GitHub: @[mahmoudr00t](https://github.com/mahmoudr00t)

