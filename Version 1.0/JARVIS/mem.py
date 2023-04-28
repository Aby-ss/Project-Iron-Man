import psutil
import shutil
import platform
from time import sleep

from rich.traceback import install
from rich import print
from rich import box
from rich.panel import Panel
from rich.table import Table

install(show_locals = True)

def MEM(mem_usage, bars = 50):
    
    path = "C:/Users/hadir"
  
    # Get the disk usage statistics
    # about the given path
    stat = shutil.disk_usage(path)

    mem_percent = (mem_usage / 100)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    
    mem_info = f"  MEMORY Usage : |{mem_bar}| {mem_usage:.2f}% "
    
    mem_panel = Panel(f"\n \n \n{mem_info}", border_style = "bold", box = box.SQUARE, title = f"[b]Total [C:/Users/hadir]: {stat[0]}", title_align = "left")

    return Panel(mem_panel, title = f"{stat[0]}", title_align = "left",box = box.SQUARE)

def more_mem_info():
    free_mem = psutil.virtual_memory()[4]
    used_mem = psutil.virtual_memory()[3]
    total_mem = psutil.virtual_memory()[0]  
    
    hdd = psutil.disk_usage('/') 
    
    info_panel = Panel(f"[b]Free Memory : {free_mem} Bytes 📚\nUsed Mmeory : {used_mem} Bytes 🔥\nTotal Memory : {total_mem} Bytes 💼", title = f"[b] {psutil.disk_partitions()[0][0]}", title_align = "left", subtitle = "Windows", subtitle_align = "left",box = box.SQUARE)
    
    return Panel(info_panel, title = "[b] MORE INFO ON MEMORY", box = box.SQUARE) 

more_mem_info()

    