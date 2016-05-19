#! /usr/bin/env python

import sys


if len(sys.argv) != 3:
    print "Usage: SYNScan.py <ip> <port>\n eg: SYNScan.py 192.168.1.1 80"
    sys.exit(1)

from scapy.all import *

ans,unans = sr(IP(dst=sys.argv[1])/TCP(dport=eval(sys.argv[2]), flags="S"),timeout=3)
for an in ans:
    print an
