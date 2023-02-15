#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep
from sys import exit
from random import randint
import datetime
from rich.panel import Panel


console = Console()


class ProgressBar:
    def __init__(self, task_description):
        self.task_description = task_description

    def progress_bar(self):
        try:
            for i in track(range(100), description=self.task_description):
                sleep(randint(1, 6) / 100)
                pass
        except Exception:
            console.print_exception(show_locals=True)
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)


class DisplayDns:
    def __init__(self, ip, dns, reverse_dns, ip_type):
        self.ip = str(ip)
        self.dns = str(dns)
        self.reverse_dns = str(reverse_dns)
        self.ip_type = str(ip_type)

    def show_results(self):
        try:
            panel = Panel.fit(f"""
                [bold cyan]IP Address:[/bold cyan] {self.ip}
                
[bold green]DNS:[/bold green] {self.dns}
[bold green]Reverse DNS:[/bold green] {self.reverse_dns}
[bold green]IP Type:[/bold green] {self.ip_type}
                              """)
            console.print(panel)
        except Exception:
            console.print_exception(show_locals=True)
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)


class DisplayWhois:
    def __init__(self, whois_results):
        self.whois_results = whois_results

    def check_list(self, value):
        if value == 'null' or value == [] or value == '':
            return 'None'
        elif isinstance(value, list):
            if value == [] or value == '':
                return 'None'
            elif isinstance(value[0], datetime.datetime):
                return str(value[0])
            else:
                return ', '.join(value)
        else:
            return value

    def show_results(self):
        domain = self.check_list(self.whois_results['domain_name'])
        registrar = self.check_list(self.whois_results['registrar'])
        creation_date = self.check_list(self.whois_results['creation_date'])
        expiration_date = self.check_list(
            self.whois_results['expiration_date'])
        updated_date = self.check_list(self.whois_results['updated_date'])
        name_servers = self.check_list(self.whois_results['name_servers'])
        status = self.check_list(self.whois_results['status'])
        emails = self.check_list(self.whois_results['emails'])
        dnssec = self.check_list(self.whois_results['dnssec'])
        name = self.check_list(self.whois_results['name'])
        org = self.check_list(self.whois_results['org'])
        address = self.check_list(self.whois_results['address'])
        city = self.check_list(self.whois_results['city'])
        state = self.check_list(self.whois_results['state'])
        country = self.check_list(self.whois_results['country'])
        try:
            panel = Panel.fit(f"""
[bold green]Domain[/bold green]: {domain}
[bold green]Registrar[/bold green]: {registrar}
[bold green]Creation Date[/bold green]: {creation_date}
[bold green]Expiration Date[/bold green]: {expiration_date}
[bold green]Updated Date[/bold green]: {updated_date}
[bold green]Name Servers[/bold green]: {name_servers}
[bold green]Status[/bold green]: {status}
[bold green]Emails[/bold green]: {emails}
[bold green]DNSSEC[/bold green]: {dnssec}
[bold green]Name[/bold green]: {name}
[bold green]Org[/bold green]: {org}
[bold green]Address[/bold green]: {address}
[bold green]City[/bold green]: {city}
[bold green]State[/bold green]: {state}
[bold green]Country[/bold green]: {country}
            """)
            console.print(panel)
        except Exception:
            console.print_exception(show_locals=True)
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)