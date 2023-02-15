#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from rich.console import Console


console = Console()

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
        return console.print("\t\t\t\t\t\t[bold red]Version: [/bold red]", "[bold green]1.2.0[/bold green]")
    
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
        console.print("[light_steel_blue1 bold]_[/light_steel_blue1 bold]" * 120 + "\n")