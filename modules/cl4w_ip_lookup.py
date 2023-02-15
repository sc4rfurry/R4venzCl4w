#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import socket
import ipaddress
from IPy import IP
from rich.console import Console
import whois
from art import tprint



console = Console()


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


class ascii_art:
    def __init__(self):
        pass

    def banner(self):
        tprint("--> IP Toolkit\n", font="small", chr_ignore=True)



class ReverseDNS:
    def __init__(self, ip):
        self.ip = ip

    def task_description(self):
        return "Reverse DNS Lookup"

    def get_reverse_dns(self):
        try:
            return socket.gethostbyaddr(self.ip)
        except socket.herror:
            return None
        except socket.gaierror:
            return None
        except socket.timeout:
            return None
        except Exception:
            return None
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]", "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)
        

class DnsLookup:
    def __init__(self, ip):
        self.ip = ip

    def task_description(self):
        return "DNS Lookup"

    def get_dns(self):
        try:
            return socket.gethostbyname(self.ip)
        except socket.herror:
            return None
        except socket.gaierror:
            return None
        except socket.timeout:
            return None
        except Exception as e:
            console.print(e)
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]", "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)


class ValidateIP:
    def __init__(self, ip):
        self.ip = ip

    def validate_ip(self):
        try:
            ipaddress.ip_address(self.ip)
            return True
        except ValueError:
            return False
        except Exception as e:
            console.print(e)
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]", "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)
        

class IpType:
    def __init__(self, ip):
        self.ip = ip

    def task_description(self):
        return "Getting IP Type"

    def get_ip_type(self):
        try:
            if IP(self.ip).iptype() == "PRIVATE":
                return "Private"
            elif IP(self.ip).iptype() == "PUBLIC":
                return "Public"
            else:
                return IP(self.ip).iptype()
        except Exception:
            return "Unknown"
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]", "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)


class Whois:
    def __init__(self, ip):
        self.ip = ip

    def task_description(self):
        return "Whois Lookup"

    def get_whois(self):
        try:
            global whois_results
            whois_results = whois.whois(self.ip)
            return whois_results
        except Exception:
            return None
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]", "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)