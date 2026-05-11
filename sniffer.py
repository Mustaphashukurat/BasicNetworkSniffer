from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):

    if packet.haslayer(IP):

        print("\n=== Packet Captured ===")

        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")

        if packet.payload:
            print(f"Payload: {bytes(packet.payload)}")

print("Starting packet capture...")

sniff(prn=packet_callback, store=False)