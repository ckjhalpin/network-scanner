from scapy.all import ARP, Ether, srp
import argparse
import socket
import csv

def scan_network(ip_range):
    # Create ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send packet and receive response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Parse response
    active_ips = []
    for sent, received in result:
        active_ips.append({'ip': received.psrc, 'mac': received.hwsrc})

    return active_ips

def main():
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("ip_range", help="IP range to scan")
    args = parser.parse_args()

    print(f"Scanning network: {args.ip_range}")
    active_ips = scan_network(args.ip_range)

    print("Active IP addresses:")
    for ip in active_ips:
        print(f"IP: {ip['ip']}, MAC: {ip['mac']}")

if __name__ == "__main__":
    main()