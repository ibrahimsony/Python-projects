## Linux OS local packet sniffing tool
import socket
from scapy.all import *
from scapy.layers.l2 import Ether# scapy.layers.l2 (l2=L2)

sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))#sniff from OSI L2

sniffer_socket.bind(("eth0", 0))#Establish connection

try:
    while True:
        raw_data, addr = sniffer_socket.recvfrom(65535)#receive traffic with max(65535 Bytes) 
        packet = Ether(raw_data)# Interpret data received from eth0
        print(packet.summary())
except keyboardinterrupt:
    sniffer_socket.close()
