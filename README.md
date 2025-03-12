# Python Network Scanner 🔍

## 📌 Overview
This Python script scans a given subnet for active devices and reports their IP addresses. 
It helps **network engineers & security teams** monitor live hosts and identify unauthorized devices.

## ⚙️ How It Works
1. Takes a **subnet input** (e.g., `192.168.1.0/24`).
2. Uses Python’s `socket` and `scapy` modules to send ARP requests.
3. Captures active devices & their IP addresses.
4. Displays results in a structured output.

## 🏗️ Prerequisites
- Python 3.x installed
- Install required dependencies:
  ```bash
  pip install scapy

## 🚀 Usage
- python3 network_scanner.py 192.168.1.0/24

## 🛠️ Issues & Troubleshooting
1️⃣ Script Didn’t Find Any Devices
  - Ensure your firewall allows ARP requests.
  - Run with admin/sudo privileges.
2️⃣ scapy Not Installed
 - Install manually: pip install scapy
3️⃣ Permission Denied Error
   Try running with: - sudo python3 network_scanner.py 192.168.1.0/24

## 📜 Sample Output

🔍 Scanning Network: 192.168.1.0/24
📡 Active Device Found: 192.168.1.10 (00:1A:2B:3C:4D:5E)
📡 Active Device Found: 192.168.1.20 (00:1B:2C:3D:4E:5F)
✅ Scan Complete - 2 Devices Found
