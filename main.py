#!/usr/bin/env python3
from modules.cl4w_ip_lookup import ReverseDNS, DnsLookup, ValidateIP, IpType, ascii_art, Whois
from modules.cl4w_port_scanner import PortScanner
from modules.cl4w_traceroute import ICMP, Traceroute, trc__banner__, icmp__banner__
from modules.cl4w_geoLocation import GeoLocation, geo__banner__
from modules.cl4w_badlist import BadList
from modules.cl4w_shodan import Shodan, shodan__banner__
from core.ip_lookup import ProgressBar, DisplayDns, DisplayWhois
from core.misc import Cl4w
import argparse
from sys import exit


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKCYAN = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
        self.BOLD = ''
        self.UNDERLINE = ''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="IP address to lookup")
    parser.add_argument("-d", help="Domain to Enumerate")
    args = parser.parse_args()
    Cl4w.banner(self=Cl4w)
    if args.i:
        ip = args.i
        ascii_art().banner()
        if ValidateIP(ip).validate_ip():
            for task in [DnsLookup.task_description, ReverseDNS.task_description, IpType.task_description]:
                ProgressBar(task(ip)).progress_bar()
            DisplayDns(ip, DnsLookup(ip).get_dns(), ReverseDNS(ip).get_reverse_dns(), IpType(ip).get_ip_type()).show_results()
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
        else:
            print("Invalid IP address")
            exit(1)
    elif args.d:
        domain = args.d
        print("Going to be implemented in ver: 1.3.0")
    else:
        print("Please enter an IP address or domain name")
        exit(1)




if __name__ == "__main__":
    main()
