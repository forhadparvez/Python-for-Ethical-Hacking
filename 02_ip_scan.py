#!/usr/bin/env python

import scapy.all as scapy
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--iprange", dest="iprange", help="IP Range to scan")
    (options, arguments)=parser.parse_args()
    if not options.iprange:
        parser.error("[-] Please specify an IP Range, use --help for more info.")   
    return options

def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answared_list=scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address\n")
    for element in answared_list:
        print(element[1].psrc+"\t\t"+element[1].hwsrc)

options=get_arguments()
scan(options.iprange)