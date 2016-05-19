#! /usr/bin/env python

from scapy.all import *

packet = sniff(iface="eth0", prn=lambda x:x.show())

wrpcap("temp.cap",packet)
