import psutil
import platform
from time import sleep

from rich.traceback import install
from rich import print
from rich import box
from rich.panel import Panel
from rich.table import Table

install(show_locals = True)

def more_info():
    processor = platform.processor()
    machine_type = platform.machine()
    architecture = platform.architecture()[0]
    platform_info = platform.platform()
    os = platform.system()
    
    #print(processor + " || " + machine_type + " || " + architecture + " || " + platform_info + " || " + os)
    # Intel64 Family 6 Model 126 Stepping 5, GenuineIntel || AMD64 || 64bit || Windows-10-10.0.19043-SP0 || Windows
    
    info_panel = Panel(f"[b]Processor : {processor}\nAMD version : {machine_type}\nArchitecture : {architecture}\nPlatform Info : {platform_info}\nOS : {os}", title = f"[b] {platform_info}", title_align = "left", box = box.SQUARE)
    
    return info_panel
    
