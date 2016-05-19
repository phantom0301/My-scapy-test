#! /usr/bin/env python

import sys


if len(sys.argv) != 2:
    print "Usage: TCPtaceroute.py <ip>\n eg: TCPtaceroute.py 192.168.1.1"
    sys.exit(1)

from scapy.all import *

ans,unans=sr(IP(dst=sys.argv[1], ttl=(4,25),id=RandShort())/TCP(flags=0x2),timeout=3)
for an in ans:
    print an
