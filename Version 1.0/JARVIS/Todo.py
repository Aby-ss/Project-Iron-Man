from rich import text
from rich import box
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout

from rich.live import Live
from rich.traceback import install
install(show_locals=True)
from rich.console import Console

from datetime import datetime
import numpy as np
import asciichartpy
import csv
import keyboard
from time import sleep
import psutil
import platform

layout = Layout()
console = Console()

layout.split_column(
    Layout(name = "Header", size = 3),
    Layout(name = "Body", size = 30),
    Layout(name = "Footer", size = 3)
)
layout["Body"].split_row(
    Layout(name = "To-Do"),
    Layout(name = "In Progress"),
    Layout(name = "Completed"),
    Layout(name = "Daily")
)

class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand = True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")

        grid.add_row("🧠", "[b]J.A.R.V.I.S[/] [b i red]To-Do App[/]", datetime.now().ctime().replace(":", "[blink]:[/]"))

        return Panel(grid, style = "Bold white on Black")

class Footer:
    def __rich__(self) -> Panel:
        f_grid = Table.grid(expand=True)
        f_grid.add_column(justify="left")
        f_grid.add_column(justify="center")
        f_grid.add_column(justify="right")

        f_grid.add_row("🧠", "[b]Good Day Sir, All Systems Online", "📑")

        return Panel(f_grid, style = "Bold white on black")

def test_layout_panel():
    Panel1 = Panel("- Cook Rice", style = "bold white", box = box.SQUARE)
    Panel2 = Panel("- Study Economics", style = "bold white", box = box.SQUARE)
    Panel3 = Panel("- Trading at S&P 500", style = "bold white", box = box.SQUARE)
    
    return Panel1
    return Panel2
    return Panel3
    
layout["Header"].update(Header())
layout["Footer"].update(Footer())

layout["To-Do"].update(test_layout_panel())

print(layout)