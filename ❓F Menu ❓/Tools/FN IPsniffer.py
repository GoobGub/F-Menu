from scapy.all import *
import subprocess
import os

def print_menu():
    print("\033[95m")  # Pink color for menu
    print("╔══════════════════════════╗")
    print("║   Fortnite Sniffer       ║")
    print("║ FORTNITE HAS TO BE OPEN  ║")
    print("╠══════════════════════════╣")
    print("║ 1. Sniff                 ║")
    print("║ 2. Exit                  ║")
    print("╚══════════════════════════╝")
    print("\033[0m")   # Reset color to default

def packet_handler(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        source_port = packet[UDP].sport
        dest_port = packet[UDP].dport

        # Filter for specific Fortnite ports (7777, 7778, 7788, and lobby ports 9000-9100)
        fortnite_ports = [7777, 7778, 7788] + list(range(9000, 9101))
        if dest_port in fortnite_ports:
            payload = packet[UDP].payload
            print(f"Fortnite IP Sniffed {source_ip}:{source_port} to {dest_ip}:{dest_port}: {payload}")

def sniff_fortnite_traffic():
    # Sniffing loop
    print("\033[95mSniffing...")  # Print "Sniffing" in pink
    sniff(filter="udp and ip", prn=packet_handler)

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            print("\033[94m")  # Purple color for the sniffing output
            sniff_fortnite_traffic()
        elif choice == '2':
        
            break
        else:
            print("Invalid choice. Please select again.")
