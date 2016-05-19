#! /usr/bin/env python

import sys


if len(sys.argv) != 2:
    print "Usage: IKEScan.py <ip>\n eg: IKEScan.py 192.168.1.1"
    sys.exit(1)

from scapy.all import *

ans, unans = sr(IP(dst=sys.argv[1])/UDP()
                /ISAKMP(init_cookie=RandString(8),exch_type="identity prot.")
                /ISAKMP_payload_SA(prop=ISAKMP_payload_Proposal()),timeout=3)
ans.nsummary(prn=lambda(s,r):r.src, lfilter=lambda(s,r):r.haslayer(ISAKMP))
for an in ans:
    print an
