#! /usr/bin/env python

import sys


if len(sys.argv) != 3:
    print "Usage: ACKScan.py <ip> <port>\n eg: ACKScan.py 192.168.1.1 80"
    sys.exit(1)

from scapy.all import *

ans,unans = sr(IP(dst=sys.argv[1])/TCP(dport=eval(sys.argv[2]), flags="A"),timeout=3)
for s, r in ans:
    if s[TCP].dport == r[TCP].sport:
        print str(s[TCP].dport) + "is unfiltered"
for s in unans:
    print str(s[TCP].dport) + "is filtered"
