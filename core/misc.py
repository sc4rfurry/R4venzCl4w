#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from os import path, getcwd
from sys import exit


console = Console()
wd = getcwd()


class Cl4w:
    def __init__(self):
        pass

    def ascii_art(self):
        banner = """
                        ______    ___                           _____  _    ___           
                        | ___ \  /   |                         /  __ \| |  /   |          
                        | |_/ / / /| |__   __  ___  _ __   ____| /  \/| | / /| |__      __
                        |    / / /_| |\ \ / / / _ \| '_ \ |_  /| |    | |/ /_| |\ \ /\ / /
                        | |\ \ \___  | \ V / |  __/| | | | / / | \__/\| |\___  | \ V  V / 
                        \_| \_|    |_/  \_/   \___||_| |_|/___| \____/|_|    |_/  \_/\_/
                            """
        console.print(f"[bold red]{banner}[/bold red]")

    def __description__(self):
        return console.print("\t\t[bold red]Description: [/bold red]", "[bold green]A modular framework for [yellow3 bold]Pentesting[/yellow3 bold] and [yellow3 bold]Bug Hunting[/yellow3 bold] written in python.[/bold green]")

    def __version__(self):
        return console.print("\t\t\t\t\t\t[bold red]Version: [/bold red]", "[bold green]1.2.1[/bold green]")

    def __author__(self):
        return console.print("\t\t\t\t\t\t[bold red]Author: [/bold red]", "[bold green]@sc4rfurry[/bold green]")

    def __license__(self):
        return console.print("\t\t\t\t\t\t[bold red]License: [/bold red]", "[bold green]MIT[/bold green]")

    def __email__(self):
        return console.print("\t\t\t\t\t\t[bold red]Email: [/bold red]", "[bold green]akalucifr@protonmail.ch[/bold green]")

    def __github__(self):
        return console.print("\t\t\t\t\t\t[bold red]Github: [/bold red]", "[bold green]https://github.com/sc4rfurry[/bold green]")

    def banner(self):
        self.ascii_art(self)
        self.__description__(self)
        print("\n")
        self.__version__(self)
        self.__author__(self)
        self.__license__(self)
        self.__email__(self)
        self.__github__(self)
        console.print(
            "[light_steel_blue1 bold]_[/light_steel_blue1 bold]" * 120 + "\n")


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


class Readme:
    def __init__(self):
        self.__path__ = path.join(wd, "README.md")

    def render(self):
        try:
            if path.exists(self.__path__) and path.isfile(self.__path__):
                with open(self.__path__, 'r') as readme:
                    markdown = readme.read()
                panel = Panel.fit(Markdown(markdown), title="README.md", border_style="red")
                console.print(panel)
            else:
                console.print("[bold red]README.md not found![/bold red]")
                exit(1)
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)