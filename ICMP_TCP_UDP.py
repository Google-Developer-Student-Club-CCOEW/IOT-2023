#using scapy library
# install scapy with cmd pip install scapy
from scapy.all import sniff

def icmp_parser(packet):
    return {
        "type": packet[1].type,
        "code": packet[1].code,
        "checksum": packet[1].chksum,
    }

def tcp_parser(packet):
    return {
        "src_port": packet[1].sport,
        "dst_port": packet[1].dport,
        "seq": packet[1].seq,
        "ack": packet[1].ack,
    }

def udp_parser(packet):
    return {
        "src_port": packet[1].sport,
        "dst_port": packet[1].dport,
        "length": packet[1].len,
    }

def packet_callback(packet):
    protocol_data = None

    if packet.haslayer("ICMP"):
        protocol = "ICMP"
        protocol_data = icmp_parser(packet)
    elif packet.haslayer("TCP"):
        protocol = "TCP"
        protocol_data = tcp_parser(packet)
    elif packet.haslayer("UDP"):
        protocol = "UDP"
        protocol_data = udp_parser(packet)
    else:
        protocol = "Unknown"

    print(f"Protocol: {protocol}")
    if protocol_data:
        print("Parsed Data:", protocol_data)

# Start sniffing
sniff(prn=packet_callback, count=10)
