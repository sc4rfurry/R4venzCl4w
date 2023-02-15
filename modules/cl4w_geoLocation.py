#!/usr/bin/env python3
# ~*- coding: utf-8 -*-
import urllib3
from urllib3 import disable_warnings
from rich.console import Console
from art import text2art
from os import name as nm
from user_agent import generate_user_agent
import json


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


disable_warnings()
os = nm
user_agent = generate_user_agent(os="win")
console = Console()


def geo__banner__():
    banner = text2art("GeoLocation", font="small")
    print(f"\n{bcolors.WARNING}{banner}{bcolors.ENDC}")

class GeoLocation:
    def __init__(self, ip):
        self.ip = ip

    def get_geo_location(self):
        try:
            url = f"http://ip-api.com/json/{self.ip}"
            resp = urllib3.PoolManager().request("GET", url, headers={"User-Agent": user_agent})
            data = resp.data.decode("utf-8")
            data = json.loads(data)
            ip = data["query"]
            country = data["country"]
            city = data["city"]
            isp = data["isp"]
            org = data["org"]
            region = data["regionName"]
            timezone = data["timezone"]
            zip_code = data["zip"]
            lat = data["lat"]
            lon = data["lon"]
            console.print(f"""
            [bold red]IP:[/bold red] {ip}
            [bold red]Country:[/bold red] {country}
            [bold red]City:[/bold red] {city}
            [bold red]ISP:[/bold red] {isp}
            [bold red]Organization:[/bold red] {org}
            [bold red]Region:[/bold red] {region}
            [bold red]Timezone:[/bold red] {timezone}
            [bold red]Zip Code:[/bold red] {zip_code}
            [bold red]Latitude:[/bold red] {lat}
            [bold red]Longitude:[/bold red] {lon}""")            
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)