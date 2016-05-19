#! /usr/bin/env python

import sys


if len(sys.argv) != 2:
    print "Usage: TCPPortScan.py <ip>\n eg: TCPPortScan.py 192.168.1.1"
    sys.exit(1)

from scapy.all import *

ans, unans = sr(IP(dst=sys.argv[1])/TCP(flags="S", dport=(1,1024)),timeout=3)
ans.nsummary(lfilter=lambda(s,r):(r.haslayer(TCP) and (r.getlayer(TCP).flags&2)))
for an in ans:
    print an
