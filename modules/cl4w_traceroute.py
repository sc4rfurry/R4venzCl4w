#!/usr/bin/env python3
# ~*- coding: utf-8 -*-
from subprocess import call
from shlex import split
from os import name, system
from shutil import which
from rich.console import Console
from .utils import bcolors


console = Console()
os = name
ping_path = which("ping").lower()


def trc__banner__():
    banner = """
 _____                                      _        
|_   _| _ _  __ _  __  ___  _ _  ___  _  _ | |_  ___ 
  | |  | '_|/ _` |/ _|/ -_)| '_|/ _ \| || ||  _|/ -_)
  |_|  |_|  \__,_|\__|\___||_|  \___/ \_,_| \__|\___|
  """
    print("\n", f"{bcolors.WARNING}{banner} {bcolors.ENDC}")


def icmp__banner__():
    banner = """
 ___   ___  __  __  ___         ___  _             
|_ _| / __||  \/  || _ \  ___  | _ \(_) _ _   __ _ 
 | | | (__ | |\/| ||  _/ |___| |  _/| || ' \ / _` |
|___| \___||_|  |_||_|         |_|  |_||_||_|\__, |
                                             |___/     
"""
    print("\n", f"{bcolors.WARNING}{banner} {bcolors.ENDC}")


class Traceroute:
    def __init__(self, host):
        self.host = host

    def get_traceroute(self):
        try:
            if os == "nt":
                if which("tracert") is not None:
                    traceroute_path = which("tracert").lower()
                else:
                    print(
                        f"\n{bcolors.OKCYAN}{bcolors.UNDERLINE}tracert.exe{bcolors.FAIL} not found{bcolors.ENDC}")
                    print(
                        f"{bcolors.FAIL}Traceroute {bcolors.ENDC} -- {bcolors.WARNING}Skipped{bcolors.ENDC}")
            else:
                if which("traceroute") is not None:
                    traceroute_path = which("traceroute")
                else:
                    print(
                        f"\n{bcolors.OKCYAN}{bcolors.UNDERLINE}traceroute{bcolors.FAIL} not found{bcolors.ENDC}")
                    print(
                        f"{bcolors.OKGREEN}You can download it using apt {bcolors.ENDC} --> {bcolors.OKCYAN}sudo apt-get install traceroute{bcolors.ENDC}")
                    print(
                        f"{bcolors.FAIL}Traceroute {bcolors.ENDC} -- {bcolors.WARNING}Skipped{bcolors.ENDC}")
            cmd = f"{traceroute_path} {self.host}"
            if os == "nt":
                cmd = f"{traceroute_path} {self.host}"
                system(cmd)
            else:
                cmd = split(cmd)
                call(cmd)
        except FileNotFoundError:
            console.print(f"[red]Error: traceroute not found[/red]")
            exit(1)
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)


class ICMP:
    def __init__(self, host):
        self.host = host

    def get_icmp(self):
        try:
            if os == "nt":
                cmd = f"{ping_path} {self.host}"
                system(cmd)
            else:
                cmd = f"{ping_path} -c 4 {self.host}"
                cmd = split(cmd)
                call(cmd)
        except Exception as e:
            if "ping: icmp open socket: Operation not permitted" in str(e):
                console.print("[red]Error: You must be root to use ping[/red]")
                exit(1)
            console.print(f"[red]Error: {e}[/red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)
