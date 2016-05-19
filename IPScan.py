#! /usr/bin/env python

import sys


if len(sys.argv) != 2:
    print "Usage: IPScan.py <ip>\n eg: IPScan.py 192.168.1.1"
    sys.exit(1)

from scapy.all import *

ans, unans = sr(IP(dst=sys.argv[1], proto=(0,255))/"SCAPY", retry=2, timeout=3)
for an in ans:
    print an.show()
