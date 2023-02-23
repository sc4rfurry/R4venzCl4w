#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import name as nm, remove as rm, path, getcwd
from rich.console import Console

os = nm
wd = getcwd()
console = Console()


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


class DoClean:
    def __init__(self):
        if os == "nt":
            self.path = path.join(wd, "core", "arsenal")
            self.path = r'"' + self.path + r'"'
        else:
            self.path = path.join(wd, "core", "arsenal")
        self.files = ["asnmap_1.0.0_linux_amd64.zip", "LICENSE", "README.md"]

    def clean(self):
        try:
            for file in self.files:
                if path.exists(path.join(self.path, file)) and path.isfile(path.join(self.path, file)):
                    rm(path.join(self.path, file))
                else:
                    pass
        except Exception as e:
            console.print(f"\n[bold red]Error: {e}[/bold red]")
            exit(1)
        except KeyboardInterrupt:
            console.print("\n[yellow bold]" + "[~] " + "[/yellow bold]",
                          "[red bold]Keyboard Interrupted[/red bold]", style="blink")
            exit(1)
