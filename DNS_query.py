#! /usr/bin/env python

import sys


if len(sys.argv) != 2:
    print "Usage: DNS_query <name>\n eg: DNS_query.py www.baidu.com"
    sys.exit(1)

from scapy.all import *

ans = sr1(IP(dst="114.114.114.114")/UDP()/DNS(rd=1,qd=DNSQR(qname=sys.argv[1])),timeout=3)
ans.show()
