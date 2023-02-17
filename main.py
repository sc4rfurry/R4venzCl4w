#!/usr/bin/env python3
# ~*- coding: utf-8 -*-
from modules.cl4w_ip_lookup import ReverseDNS, DnsLookup, ValidateIP, IpType, ascii_art, Whois
from modules.cl4w_port_scanner import PortScanner
from modules.cl4w_traceroute import ICMP, Traceroute, trc__banner__, icmp__banner__
from modules.cl4w_geoLocation import GeoLocation, geo__banner__
from modules.cl4w_badlist import BadList
from modules.cl4w_shodan import Shodan, shodan__banner__
from modules.cl4w_offensive import Offensive, o3__banner__
from modules.cl4w_fetch_proxies import ProxyNinja, xxx__banner__
from modules.cl4w_asnlookup import AsnLookup, asn__banner__
from core.ip_lookup import ProgressBar, DisplayDns, DisplayWhois
from core.misc import Cl4w, Readme
import argparse
from sys import exit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="IP address to lookup")
    parser.add_argument("-d", help="Domain to Enumerate")
    parser.add_argument(
        "-x", help="Run Host Enumeration on IP, Domain, IP Range, or Selected IP's. example: 192.168.11.11 | 142.250.181.174-255 | 192.168.11.11,192.168.11.12")
    parser.add_argument("-fp", help="Fetch https/socks4 Proxies")
    parser.add_argument(
        "-r", help="Displays the Readme file", action='store_true')
    args = parser.parse_args()
    Cl4w.banner(self=Cl4w)
    if args.i:
        ip = args.i
        ascii_art().banner()
        if ValidateIP(ip).validate_ip():
            for task in [DnsLookup.task_description, ReverseDNS.task_description, IpType.task_description]:
                ProgressBar(task(ip)).progress_bar()
            DisplayDns(ip, DnsLookup(ip).get_dns(), ReverseDNS(
                ip).get_reverse_dns(), IpType(ip).get_ip_type()).show_results()
            for task in [Whois.task_description]:
                ProgressBar(task(ip)).progress_bar()
            DisplayWhois(Whois(ip).get_whois()).show_results()
            host = str(ip)
            PortScanner(host).get_port_status()
            trc__banner__()
            Traceroute(host).get_traceroute()
            icmp__banner__()
            ICMP(host).get_icmp()
            geo__banner__()
            GeoLocation(ip).get_geo_location()
            BadList(ip).bl__check__()
            shodan__banner__()
            Shodan(ip).get_results()
            asn__banner__()
            AsnLookup(ip).asnmap()
        else:
            print("Invalid IP address")
            exit(1)
    elif args.d:
        domain = args.d
        print("Going to be implemented in ver: 1.3.0")
    elif args.x:
        input = args.x
        o3__banner__()
        Offensive(input).o3__scan__()
    elif args.r:
        Readme().render()
    elif args.fp:
        proxy_type = args.fp
        xxx__banner__()
        print(ProxyNinja(proxy_type).get_proxies())

    else:
        print("Please enter an IP address or domain name")
        exit(1)


if __name__ == "__main__":
    main()
