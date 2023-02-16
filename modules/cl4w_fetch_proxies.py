#!/usr/bin/env python3
# ~*- coding: utf-8 -*-
from proxy_ninja_ng import fetch_proxies_list, fetch_proxies_json
from core.misc import bcolors
from rich.console import Console
from art import text2art
from sys import exit
from emoji import emojize


console = Console()


def xxx__banner__():
    banner = text2art("ProxyNinja-ng", font="small")
    print(f"\n{bcolors.WARNING}{banner}{bcolors.ENDC}")
    print(emojize(
        f"\t:Japanese_secret_button:  {bcolors.OKBLUE}{bcolors.BOLD}ProxyNinja-ng{bcolors.ENDC} --> {bcolors.WARNING}{bcolors.BOLD}Fetches Public Proxies {bcolors.ENDC}: {bcolors.OKCYAN}https/socks4{bcolors.ENDC}"))
    print(
        f"\n\t{bcolors.OKGREEN}[+]{bcolors.ENDC} {bcolors.OKCYAN}ProxyNinja-ng {bcolors.ENDC} -- {bcolors.OKGREEN}Loaded{bcolors.ENDC}\n")


# fetch_proxies_list(PROXY_TYPE) returns a list of proxies
# fetch_proxies_json(PROXY_TYPE) returns a json object of proxies
# PROXY_TYPE: https/socks4
class ProxyNinja:
    def __init__(self, proxy_type):
        self.proxy_type = proxy_type

    def get_format(self):
        try:
            self.format = str(
                input(f"{bcolors.OKCYAN}Format (json/lst): {bcolors.ENDC}"))
            if self.format == "json":
                self.json = True
            elif self.format == "lst":
                self.json = False
            else:
                print(f"{bcolors.FAIL}Invalid Format{bcolors.ENDC}")
                print(
                    f"Possible Formats: {bcolors.OKCYAN}json/lst{bcolors.ENDC}")
                exit(1)
        except Exception as e:
            print(f"{bcolors.FAIL}Error: {e}{bcolors.ENDC}")
            exit(1)
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)

    def get_proxies(self):
        try:
            if self.proxy_type == "https":
                self.get_format()
                if self.json:
                    return fetch_proxies_json("https")
                else:
                    return fetch_proxies_list("https")
            elif self.proxy_type == "socks4":
                self.get_format()
                if self.json:
                    return fetch_proxies_json("socks4")
                else:
                    return fetch_proxies_list("socks4")
            else:
                print(f"{bcolors.FAIL}Invalid Proxy Type{bcolors.ENDC}")
                print(
                    f"Possible Proxy Types: {bcolors.OKCYAN}https/socks4{bcolors.ENDC}")
                exit(1)
        except TypeError:
            print(f"{bcolors.FAIL}No Proxies Found{bcolors.ENDC}")
            exit(1)
        except Exception:
            if "'NoneType' has no attribute":
                print(f"{bcolors.FAIL}No Proxies Found{bcolors.ENDC}")
                exit(1)
            else:
                return None
        except KeyboardInterrupt:
            console.print("[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)
