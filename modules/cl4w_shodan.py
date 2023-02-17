#!/usr/bin/env python3
# ~*- coding: utf-8 -*-
from rich.console import Console
from rich.panel import Panel
from os import name as nm, environ, path, getcwd
from load_xl import read_config_file
from .utils import bcolors


try:
    import shodan
except ImportError:
    print("Please install shodan module")
    print("python3 -m pip install shodan")
    print(f"{bcolors.FAIL}Error {bcolors.ENDC} --> {bcolors.WARNING}(Fatal Error ..!){bcolors.ENDC}")
    exit(1)


console = Console()
os = nm
wd = getcwd()
config_file = path.join(wd, ".configx")
if path.exists(config_file) and path.isfile(config_file):
    config = read_config_file(config_file)
    if "SHODAN_API_KEY" in environ:
        shodan_api_key = environ['SHODAN_API_KEY']
    else:
        shodan_api_key = None
else:
    shodan_api_key = "null"
    pass


def shodan__banner__():
    banner = """
 ___  _             _             
/ __|| |_   ___  __| | __ _  _ _  
\__ \| ' \ / _ \/ _` |/ _` || ' \ 
|___/|_||_|\___/\__,_|\__,_||_||_|
"""
    print(f"{bcolors.WARNING}{banner} {bcolors.ENDC}")


class Shodan:
    def __init__(self, ip):
        self.api_key = shodan_api_key
        self.ip = ip

    def get_results(self):
        try:
            if self.api_key is None:
                print(
                    f"{bcolors.FAIL}Error: SHODAN_API_KEY is not set in config file{bcolors.ENDC}")
                print(
                    f"{bcolors.FAIL}Shodan Scan {bcolors.ENDC} -- {bcolors.WARNING}Skipped{bcolors.ENDC}")
                return
            elif self.api_key == "null":
                print(f"\n{bcolors.FAIL}Config File not found{bcolors.ENDC}")
                print(
                    f"{bcolors.FAIL}Please make sure to create a .configx file{bcolors.ENDC}")
                print(
                    f"{bcolors.FAIL}Shodan Scan {bcolors.ENDC} -- {bcolors.WARNING}Skipped{bcolors.ENDC}")
                return
            else:
                api = shodan.Shodan(self.api_key)
                host = api.host(self.ip)
                console.print(Panel.fit("""
        [green bold]Hostname:[/green bold] [cyan bold]{}[/cyan bold]
        [green bold]Ports:[/green bold] [yellow3]{}[/yellow3]
        [green bold]Domains:[/green bold] [yellow3]{}[/yellow3]
        [green bold]Country:[/green bold] [yellow3]{}[/yellow3]
        [green bold]City:[/green bold] [yellow3]{}[/yellow3]
        [green bold]Organization:[/green bold] [yellow3]{}[/yellow3]
        [green bold]Operating System:[/green bold] [yellow3]{}[/yellow3]
        [green bold]ISP:[/green bold] [yellow3]{}[/yellow3]
        [green bold]ASN:[/green bold] [yellow3]{}[/yellow3]
            """.format(host['hostnames'], host['ports'], host['domains'], host['country_name'], host['city'], host['org'], host['os'], host['isp'], host['asn']), title="Shodan Results", title_align="center", border_style="green", padding=(1, 1)))
        except shodan.APIError as e:
            if e == "No information available for that IP.":
                print(f"{bcolors.FAIL}Error: {e}{bcolors.ENDC}")
            elif e == "Invalid API key":
                print(f"{bcolors.FAIL}Error: {e}{bcolors.ENDC}")
            else:
                print(f"{bcolors.FAIL}Error: {e}{bcolors.ENDC}")
