#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aslookup import get_as_data
from .utils import bcolors
from rich.panel import Panel
from rich.console import Console
from subprocess import check_output, PIPE
from shlex import split
from os import path, getcwd, name as nm, path, chmod, makedirs
from wget import download
from zipfile import ZipFile


console = Console()
wd = getcwd()
os = nm
bin_path = path.join(wd, "core", "arsenal")
win64_bin_url = "https://github.com/projectdiscovery/asnmap/releases/download/v1.0.0/asnmap_1.0.0_windows_amd64.zip"
linux_bin_url = "https://github.com/projectdiscovery/asnmap/releases/download/v1.0.0/asnmap_1.0.0_linux_amd64.zip"


def asn__banner__():
    banner = """
   _    ___  _  _   _               _               
  /_\  / __|| \| | | |    ___  ___ | |__ _  _  _ __ 
 / _ \ \__ \| .` | | |__ / _ \/ _ \| / /| || || '_ \\
/_/ \_\|___/|_|\_| |____|\___/\___/|_\_\ \_,_|| .__/
                                              |_|  
    """
    print("\n" + bcolors.BOLD + bcolors.WARNING + banner + bcolors.ENDC)
    print("\t\t" + bcolors.HEADER + "Asn Lookup Tool. " + bcolors.ENDC +
          f"({bcolors.OKGREEN} Ip2Asn{bcolors.ENDC}/{bcolors.OKGREEN} ASN to CIDR's{bcolors.ENDC} )" + "\n")


class Ip2Asn:
    def __init__(self, ip):
        self.ip = ip

    def get_asn(self):
        try:
            data = get_as_data(self.ip, service="shadowserver")
            data = list(data)
            console.print(Panel.fit(f"""
[bold yellow3]ASN:[/bold yellow3] {data[0]}
[bold yellow3]AS Name:[/bold yellow3] {data[2]}
[bold yellow3]Prefix:[/bold yellow3] {data[5]}
[bold yellow3]Country:[/bold yellow3] {data[6]}
[bold yellow3]Organization:[/bold yellow3] {data[8]}

[bold cyan]Data Source:[/bold cyan] [bold underline green]{data[9]}[/bold underline green]
            """, title="[bold cyan]Ip2Asn[/bold cyan]", border_style="bold red", padding=(0, 2), title_align="center"))
            return data
        except Exception as e:
            console.print(f"\n[bold red]Error: {e}[/bold red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)


class AsnLookup:
    def __init__(self, ip):
        self.ip = ip
        asn = Ip2Asn(self.ip)
        self._asn = asn.get_asn()
        self.asn = str(self._asn[0])
        if self.asn == "None" or self.asn == "":
            console.print("[bold red]ASN not found![/bold red]")
            exit(1)

    def check_dir_struct(self):
        if os == "nt":
            dir_path = path.join(wd, "core", "arsenal")
            dir_path = r'"' + dir_path + r'"'
        else:
            dir_path = path.join(wd, "core", "arsenal")
        try:
            if path.exists(dir_path) and path.isdir(dir_path):
                return True
            else:
                print(
                    f"\n{bcolors.OKCYAN}[*] Creating directory structure...{bcolors.ENDC}")
                print(
                    f"{bcolors.OKCYAN}[*] Creating {bin_path}...{bcolors.ENDC}")
                makedirs(bin_path)
                return True
        except Exception as e:
            console.print(f"\n[bold red]Error: {e}[/bold red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)

    def download_bins(self):
        if os == "nt":
            try:
                __path = path.join(bin_path, "asnmap.exe")
                __path__ = r'"' + __path__ + r'"'
                if path.exists(__path__) and path.isfile(__path__):
                    print(
                        f"\n\n  {bcolors.OKGREEN}[*] AsnMap found..!{bcolors.ENDC}")
                    return True
                else:
                    print(
                        f"\n{bcolors.FAIL}[~] AsnMap not found..!{bcolors.ENDC}")
                    print(
                        f"{bcolors.OKCYAN}[*] Downloading AsnMap_amd64...{bcolors.ENDC}")
                    download(win64_bin_url, out=bin_path)
                    cmd = f'unzip {bin_path}\\asnmap_1.0.0_linux_amd64.zip -d {bin_path}'
                    check_output(split(cmd), shell=True, stderr=PIPE)
            except Exception as e:
                console.print(f"\n[bold red]Error: {e}[/bold red]")
                exit(1)
            except KeyboardInterrupt:
                console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                              "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                exit(1)
        else:
            try:
                __path = path.join(bin_path, "asnmap")
                if path.exists(__path) and path.isfile(__path):
                    print(
                        f"\n\n  {bcolors.OKGREEN}[*] AsnMap found..!{bcolors.ENDC}")
                    return True
                else:
                    print(
                        f"\n{bcolors.FAIL}[~] AsnMap not found..!{bcolors.ENDC}")
                    print(
                        f"{bcolors.OKCYAN}[*] Downloading AsnMap_amd64...{bcolors.ENDC}")
                    download(linux_bin_url, out=bin_path)
                    try:
                        with ZipFile(f"{bin_path}/asnmap_1.0.0_linux_amd64.zip", 'r') as zipObj:
                            zipObj.extractall(bin_path)
                    except Exception as e:
                        console.print(f"\t[bold red]Error: {e}[/bold red]")
                        exit(1)
                    return True
            except Exception as e:
                console.print(f"\n[bold red]Error: {e}[/bold red]")
                exit(1)
            except KeyboardInterrupt:
                console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                              "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                exit(1)

    def asnmap(self):
        asnmap = path.join(bin_path, "asnmap")
        if os == "nt":
            try:
                if self.check_dir_struct():
                    if self.download_bins():
                        asnmap = asnmap + ".exe"
                        asnmap = r'"' + asnmap + r'"'
                        _output = check_output(
                            split(f"{asnmap} -a {self.asn} -silent"), stderr=PIPE, stdin=PIPE)
                        console.print("\n", Panel.fit(f"""
    [bold yellow3]ASN:[/bold yellow3] {self._asn[0]}
    [bold yellow3]Lookup Details:[/bold yellow3]

{_output.decode("utf-8")}""", title="[bold cyan]ASN Lookup[/bold cyan]", border_style="bold red", padding=(0, 2), title_align="center"))
                    else:
                        console.print(
                            f"\n[bold red]Error: Binaries are missing.[/bold red]")
                        exit(1)
                else:
                    console.print(
                        f"\n[bold red]Error: Directory structure is missing.[/bold red]")
                    exit(1)
            except Exception as e:
                console.print(f"\n[bold red]Error: {e}[/bold red]")
                exit(1)
            except KeyboardInterrupt:
                console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                              "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                exit(1)
        else:
            try:
                if self.check_dir_struct():
                    if self.download_bins():
                        perms = "777"
                        chmod(asnmap, int(perms, 8))
                        _output = check_output(
                            split(f"{asnmap} -a {self.asn} -silent"), stderr=PIPE, stdin=PIPE)
                        console.print("\n", Panel.fit(f"""
    [bold yellow3]ASN:[/bold yellow3] {self._asn[0]}
    [bold yellow3]Lookup Details:[/bold yellow3]

{_output.decode("utf-8")}""", title="[bold cyan]ASN Lookup[/bold cyan]", border_style="bold red", padding=(0, 2), title_align="center"))
                    else:
                        console.print(
                            f"\n[bold red]Error: Binaries are missing.[/bold red]")
                        exit(1)
                else:
                    console.print(
                        f"\n[bold red]Error: Directory structure is missing.[/bold red]")
                    exit(1)
            except Exception as e:
                console.print(f"\n[bold red]Error: {e}[/bold red]")
                exit(1)
            except KeyboardInterrupt:
                console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                              "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                exit(1)
