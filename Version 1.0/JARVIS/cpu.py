import psutil
import platform
from time import sleep

from rich.traceback import install
from rich import print
from rich import box
from rich.panel import Panel
from rich.table import Table

install(show_locals = True)

def cpu_usage(cpu_usage, bars = 50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    cpu_info = f"CPU Usage : |{cpu_bar}| {cpu_usage:.2f}% "
    return cpu_info

    
def mem_usage(mem_usage, bars = 50):
    
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    mem_info = f"MEMORY Usage : |{mem_bar}| {mem_percent:.2f}% "
    return mem_info

def CPU(cpu_usage, bars = 50):   
    cpu_name = platform.processor() 
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    
    cpu_info = f"    CPU Usage : |{cpu_bar}| {cpu_usage:.2f}% "
    
    cpu_panel = Panel(f"\n \n \n{cpu_info}", border_style = "bold", box = box.SQUARE)

    return Panel(cpu_panel, title = f"{cpu_name}", title_align = "left",box = box.SQUARE)

def per_CPU():
    num_cores = psutil.cpu_count(logical=False)
    num_threads = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq()[0]
    per_cpu_percent = psutil.cpu_percent(percpu= True)
    
    per_cpu_info = Panel(f" \n[b]Core 1: {per_cpu_percent[0]}       Core 5: {per_cpu_percent[4]}\nCore 2: {per_cpu_percent[1]}      Core 6: {per_cpu_percent[5]}\nCore 3: {per_cpu_percent[2]}      Core 7: {per_cpu_percent[6]}\nCore 4: {per_cpu_percent[3]}      Core 8: {per_cpu_percent[7]}", title_align = "left", subtitle = f"{cpu_freq} MHz", subtitle_align = "left", box = box.SQUARE)
    
    return Panel(per_cpu_info, title = "[b] MORE INFO ON CPU", box = box.SQUARE)
    
CPU(psutil.cpu_percent(), 50)
