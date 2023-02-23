#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .utils import bcolors
from subprocess import call, PIPE
from shlex import split
from os import path, getcwd, name as nm, path, chmod, makedirs
from wget import download
from rich.console import Console
from .utils import bcolors
from requests import Session
from tldextract import extract

console = Console()
wd = getcwd()
os = nm
git_api = "https://api.github.com/repos/sc4rfurry/Curs3AF/releases/latest"
if os == "nt":
    bin_path = path.join(wd, "core", "arsenal")
    bin_path = r'"' + bin_path + r'"'
else:
    bin_path = path.join(wd, "core", "arsenal")


def get_latest_release():
    global bin_url, latest_release
    try:
        with Session() as s:
            s.headers.update({"Accept": "application/vnd.github.v3+json"})
            response = s.get(git_api)
            if response.status_code == 200:
                latest_release = response.json()["tag_name"]
                if os == "nt":
                    bin_url = f"https://github.com/sc4rfurry/Curs3AF/releases/download/{latest_release}/curs3af-windows-amd64.exe"
                else:
                    bin_url = f"https://github.com/sc4rfurry/Curs3AF/releases/download/{latest_release}/curs3af-linux-amd64"
                return bin_url, latest_release
            else:
                console.print(
                    f"\n[bold red]Error: Could not fetch the latest Release.[/bold red] [cyan bold]Status Code:[/cyan bold]{response.status_code}")
                console.print(
                    f"\n[bold yellow]Error: Using the default Release.[/bold yellow] [cyan bold]Version:[/cyan bold] 1.0.1")
                if os == "nt":
                    bin_url = f"https://github.com/sc4rfurry/Curs3AF/releases/download/v1.0.1/curs3af-windows-amd64.exe"
                else:
                    bin_url = f"https://github.com/sc4rfurry/Curs3AF/releases/download/v1.0.1/curs3af-linux-amd64"
                return bin_url, latest_release
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/bold red]")
        exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                      "[red bold]Keyboard Interrupted[/red bold]", style="blink")
        exit(1)


class Curs3AF:
    def __init__(self):
        pass

    def __nah__(self):
        get_latest_release()
        self.url = str(bin_url)
        self.release = str(latest_release)

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
        self.__nah__()
        if os == "nt":
            try:
                __path = path.join(bin_path, "curs3af-windows-amd64.exe")
                __path__ = r'"' + __path__ + r'"'
                if path.exists(__path__) and path.isfile(__path__):
                    print(
                        f"\n\n  {bcolors.OKGREEN}[*] Curs3AF found..!{bcolors.ENDC}")
                    return True
                else:
                    print(
                        f"\n{bcolors.FAIL}[~] Curs3AF not found..!{bcolors.ENDC}")
                    print(
                        f"{bcolors.OKCYAN}[*] Downloading Curs3AF...{bcolors.ENDC}")
                    download(self.url, out=bin_path)
            except Exception as e:
                console.print(f"\n[bold red]Error: {e}[/bold red]")
                exit(1)
            except KeyboardInterrupt:
                console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                              "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                exit(1)
        else:
            try:
                __path = path.join(bin_path, "curs3af-linux-amd64")
                if path.exists(__path) and path.isfile(__path):
                    print(
                        f"\n\n  {bcolors.OKGREEN}[*] Curs3AF found..!{bcolors.ENDC}")
                    return True
                else:
                    print(
                        f"\n{bcolors.FAIL}[~] Curs3AF not found..!{bcolors.ENDC}")
                    print(
                        f"{bcolors.OKCYAN}[*] Downloading Curs3AF...{bcolors.ENDC}")
                    download(self.url, out=bin_path)
                    return True
            except Exception as e:
                console.print(f"\n[bold red]Error: {e}[/bold red]")
                exit(1)
            except KeyboardInterrupt:
                console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                              "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                exit(1)


class Fingerprint:
    def __init__(self):
        Curs3AF().check_dir_struct()
        Curs3AF().download_bins()

    def check_file(self):
        try:
            if path.exists(self.file) and path.isfile(self.file):
                return True
            else:
                print(
                    f"\n{bcolors.BOLD}{bcolors.FAIL}[~] File not found..!{bcolors.ENDC} -- {self.file}")
                exit(1)
        except Exception as e:
            console.print(f"\n[bold red]Error: {e}[/bold red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)

    def run(self):
        try:
            self.isGeneric = input(
                f"\n\n{bcolors.BOLD}{bcolors.OKBLUE}[+]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKCYAN}Do you wanna run Generic Scan (y/n):{bcolors.ENDC} ")
            isSingle = input(
                f"{bcolors.BOLD}{bcolors.OKBLUE}[+]{bcolors.ENDC} {bcolors.BOLD}{bcolors.OKCYAN}Do you wanna Scan Single Domain or Multiple (s/f):{bcolors.ENDC} ")
            if self.isGeneric.lower() == "y" or self.isGeneric.lower() == "yes":
                if isSingle.lower() == "s" or isSingle.lower() == "single":
                    self.url = input(
                        f"\n{bcolors.BOLD}{bcolors.OKBLUE}[+]{bcolors.ENDC} {bcolors.BOLD}{bcolors.HEADER}Enter URL to Scan (example.com):{bcolors.ENDC} ")
                    tsd, td, tsu = extract(self.url)
                    self.url = td + '.' + tsu
                elif isSingle.lower() == "f" or isSingle.lower() == "file":
                    self.file = input(
                        f"\n{bcolors.BOLD}{bcolors.OKBLUE}[+]{bcolors.ENDC} {bcolors.BOLD}{bcolors.HEADER}Enter Path to File:{bcolors.ENDC} ")
                else:
                    console.print(
                        f"\n{bcolors.BOLD}{bcolors.FAIL}[~] Invalid Input..!{bcolors.ENDC}")
                    exit(1)
            elif self.isGeneric.lower() == "n" or self.isGeneric.lower() == "no":
                if isSingle.lower() == "s" or isSingle.lower() == "single":
                    self.url = input(
                        f"\n{bcolors.BOLD}{bcolors.OKBLUE}[+]{bcolors.ENDC} {bcolors.BOLD}{bcolors.HEADER}Enter URL to Scan (example.com):{bcolors.ENDC} ")
                    tsd, td, tsu = extract(self.url)
                    self.url = td + '.' + tsu
                elif isSingle.lower() == "f" or isSingle.lower() == "file":
                    self.file = input(
                        f"\n{bcolors.BOLD}{bcolors.OKBLUE}[+]{bcolors.ENDC} {bcolors.BOLD}{bcolors.HEADER}Enter Path to File:{bcolors.ENDC} ")
                else:
                    console.print(
                        f"\n{bcolors.BOLD}{bcolors.FAIL}[~] Invalid Input..!{bcolors.ENDC}")
                    exit(1)
            else:
                console.print(
                    f"\n{bcolors.BOLD}{bcolors.FAIL}[~] Invalid Input..!{bcolors.ENDC}")
                exit(1)
            if os == "nt":
                if isSingle.lower() == "s" or isSingle.lower() == "single":
                    try:
                        if self.isGeneric:
                            cmd = f"{bin_path}\\curs3af-windows-amd64.exe -u {self.url} -g"
                        else:
                            cmd = f"{bin_path}\\curs3af-windows-amd64.exe -u {self.url}"
                        call(split(cmd), cwd=bin_path)
                    except Exception as e:
                        console.print(f"\n[bold red]Error: {e}[/bold red]")
                        exit(1)
                    except KeyboardInterrupt:
                        console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                                      "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                        exit(1)
                else:
                    try:
                        if self.check_file():
                            if self.isGeneric:
                                cmd = f"{bin_path}\\curs3af-windows-amd64.exe -f {self.file} -g"
                            else:
                                cmd = f"{bin_path}\\curs3af-windows-amd64.exe -f {self.file}"
                            call(split(cmd), cwd=bin_path)
                        else:
                            print(
                                f"\n{bcolors.BOLD}{bcolors.FAIL}[~] File not found..!{bcolors.ENDC} -- {self.file}")
                            exit(1)
                    except Exception as e:
                        console.print(f"\n[bold red]Error: {e}[/bold red]")
                        exit(1)
                    except KeyboardInterrupt:
                        console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                                      "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                        exit(1)
            else:
                if isSingle.lower() == "s" or isSingle.lower() == "single":
                    try:
                        if self.isGeneric:
                            cmd = f"{bin_path}/curs3af-linux-amd64 -u {self.url} -g"
                        else:
                            cmd = f"{bin_path}/curs3af-linux-amd64 -u {self.url}"
                        perms = "777"
                        chmod(bin_path + "/curs3af-linux-amd64", int(perms, 8))
                        call(split(cmd), cwd=bin_path)
                    except Exception as e:
                        console.print(f"\n[bold red]Error: {e}[/bold red]")
                        exit(1)
                    except KeyboardInterrupt:
                        console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                                      "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                        exit(1)
                else:
                    try:
                        if self.check_file():
                            if self.isGeneric:
                                cmd = f"{bin_path}/curs3af-linux-amd64 -f {self.file} -g"
                            else:
                                cmd = f"{bin_path}/curs3af-linux-amd64 -f {self.file}"
                            perms = "777"
                            chmod(bin_path + "/curs3af-linux-amd64", int(perms, 8))
                            call(split(cmd), cwd=bin_path)
                        else:
                            print(
                                f"\n{bcolors.BOLD}{bcolors.FAIL}[~] File not found..!{bcolors.ENDC} -- {self.file}")
                            exit(1)
                    except Exception as e:
                        console.print(f"\n[bold red]Error: {e}[/bold red]")
                        exit(1)
                    except KeyboardInterrupt:
                        console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                                      "[red bold]Keyboard Interrupted[/red bold]", style="blink")
                        exit(1)
        except Exception as e:
            console.print(f"\n[bold red]Error: {e}[/bold red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)
