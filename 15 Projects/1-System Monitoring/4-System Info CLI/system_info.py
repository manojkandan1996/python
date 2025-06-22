import platform
import psutil
import os

def display_system_info():
    print("====== System Information ======")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    
    print("\n====== CPU Info ======")
    print(f"Cores (Physical): {psutil.cpu_count(logical=False)}")
    print(f"Cores (Logical):  {psutil.cpu_count(logical=True)}")
    print(f"CPU Frequency:    {psutil.cpu_freq().current:.2f} MHz")
    print(f"CPU Usage:        {psutil.cpu_percent(interval=1)}%")

    print("\n====== Memory Info ======")
    mem = psutil.virtual_memory()
    print(f"Total RAM:        {mem.total // (1024**3)} GB")
    print(f"Used RAM:         {mem.used // (1024**3)} GB")
    print(f"Available RAM:    {mem.available // (1024**3)} GB")
    print(f"RAM Usage:        {mem.percent}%")

display_system_info()