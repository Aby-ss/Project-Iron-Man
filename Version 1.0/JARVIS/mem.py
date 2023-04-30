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

def more_info(mem_usage, bars = 50):
    processor = platform.processor()
    machine_type = platform.machine()
    architecture = platform.architecture()[0]
    platform_info = platform.platform()
    os = platform.system()
    
    free_mem = psutil.virtual_memory()[4]
    used_mem = psutil.virtual_memory()[3]
    total_mem = psutil.virtual_memory()[0]  
    
    hdd = psutil.disk_usage('/') 
    
    path = "C:/Users/hadir"
  
    # Get the disk usage statistics
    # about the given path
    stat = shutil.disk_usage(path)

    mem_percent = (mem_usage / 100)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    
    mem_info = f"  MEMORY Usage : |{mem_bar}| {mem_usage:.2f}% "
    
    mem_panel = Panel(f"\n \n \n{mem_info}", border_style = "bold", box = box.SQUARE, title = f"[b]Total [C:/Users/hadir]: {stat[0]}", title_align = "left")
    
    #print(processor + " || " + machine_type + " || " + architecture + " || " + platform_info + " || " + os)
    # Intel64 Family 6 Model 126 Stepping 5, GenuineIntel || AMD64 || 64bit || Windows-10-10.0.19043-SP0 || Windows
    
    info_panel = Panel(f"[b]Processor : {processor}\nAMD version : {machine_type}\nArchitecture : {architecture}\nPlatform Info : {platform_info}\nOS : {os}\n\n\n[b]Free Memory : {free_mem} Bytes 📚\nUsed Mmeory : {used_mem} Bytes 🔥\nTotal Memory : {total_mem} Bytes 💼\n\n\n\n {mem_info}", title = f"[b] {platform_info}", title_align = "left", box = box.SQUARE)
    
    return info_panel

more_mem_info()

    