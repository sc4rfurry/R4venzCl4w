#!/usr/bin/env python3
# ~*- coding: utf-8 -*-

from rich.console import Console
from shlex import split
from subprocess import call
from os import path, getcwd, system, name
import re
from sys import exit
from core.misc import bcolors
import wget
from shutil import which


validate_ip = re.compile(
    r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
validate_cidr = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.)(\d{1,3})-(\d{1,3})$')
win64_bin_url = "https://github.com/shadow1ng/fscan/releases/download/1.8.2/fscan64.exe"
linux_bin_url = "https://github.com/shadow1ng/fscan/releases/download/1.8.2/fscan_amd64"
os = name
wd = getcwd()
_chmod = which("chmod")
_chown = which("chown")
console = Console()
bin_path = path.join(wd, "core", "bin")


def o3__banner__():
    print(f"""{bcolors.OKGREEN}
  ______        ______  ___  ___ ________           _            
 / __   |      / __   |/ __)/ __|_______/          (_)           
| | //| |_   _| | //| | |__| |__   ____  ____   ___ _ _   _ ____ 
| |// | ( \ / ) |// | |  __)  __) (___ \|  _ \ /___) | | | / _  )
|  /__| |) X (|  /__| | |  | |   _____) ) | | |___ | |\ V ( (/ / 
 \_____/(_/ \_)\_____/|_|  |_|  (______/|_| |_(___/|_| \_/ \____)
{bcolors.ENDC}

        -> {bcolors.OKCYAN}An intranet comprehensive scanning tool, which is convenient for automatic and omnidirectional missed scanning.{bcolors.ENDC}
""")
    print(f"{bcolors.HEADER}={bcolors.ENDC}" * 120 + "\n")


class Offensive:
    def __init__(self, input):
        self.input = input

    def validate_input(self):
        if '-' in self.input:
            if validate_cidr.match(self.input):
                return True
            else:
                return False
        elif "," in self.input:
            return True
        elif validate_ip.match(self.input):
            return True
        else:
            return False

    def download_bin(self):
        try:
            if os == "nt":
                __path__ = path.join(wd, "core", "bin", "fscan64.exe")
                if path.exists(__path__) and path.isfile(__path__):
                    print(f"\t\t{bcolors.OKGREEN}[*] Fscan found..!{bcolors.ENDC}")
                    return
                else:
                    print(f"{bcolors.FAIL}[~] Fscan not found..!{bcolors.ENDC}")
                    print(f"{bcolors.OKCYAN}[*] Downloading fscan_amd64...{bcolors.ENDC}")
                    wget.download(win64_bin_url, bin_path)
                    cmd = f"{_chmod} +x {__path__}"
                    system(cmd)
            else:
                __path__ = path.join(wd, "core", "bin", "fscan_amd64")
                if path.exists(__path__) and path.isfile(__path__):
                    print(f"\t\t{bcolors.OKGREEN}[*] Fscan found..!{bcolors.ENDC}")
                    return
                else:
                    print(f"{bcolors.FAIL}[~] Fscan not found..!{bcolors.ENDC}")
                    print(f"{bcolors.OKCYAN}[*] Downloading fscan_amd64...{bcolors.ENDC}")
                    wget.download(linux_bin_url, bin_path)
        except Exception as e:
            print(f"{bcolors.FAIL}Error: {e} {bcolors.ENDC}")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)

    def o3__scan__(self):
        try:
            self.download_bin()
            if self.validate_input():
                if os == "nt":
                    __path__ = path.join(wd, "core", "bin", "fscan64.exe")
                    cmd = f"{__path__} -h {self.input} -full -no"
                    system(cmd)
                else:
                    __path__ = path.join(wd, "core", "bin", "fscan_amd64")
                    cmd = f"{_chmod} +x {__path__}"
                    cmd = split(cmd)
                    call(cmd)
                    cmd = f"{_chmod} +x {bin_path}"
                    cmd = f"{__path__} -h {self.input} -full -no"
                    cmd = split(cmd)
                    call(cmd)
            else:
                print(f"{bcolors.FAIL}[-] Invalid input{bcolors.ENDC}\n\t- {bcolors.OKCYAN}example:{bcolors.ENDC} {bcolors.OKBLUE}192.168.11.11{bcolors.ENDC} | {bcolors.OKBLUE}192.168.11.11-255{bcolors.ENDC} | {bcolors.OKBLUE}192.168.11.11,192.168.11.12{bcolors.ENDC}")
                exit(1)
        except Exception as e:
            print(bcolors.FAIL + "[-] Error: " + str(e) + bcolors.ENDC)
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)