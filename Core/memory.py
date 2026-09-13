import psutil

memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()

Total_Ram = memory.total / (1024 ** 3)
Available_Ram = memory.available / (1024 ** 3)
Used_Ram = memory.used / (1024 ** 3)
Ram_Percent = memory.percent

ram = {
    "total": Total_Ram,
    "available": Available_Ram,
    "used": Used_Ram,
    "percent": Ram_Percent
}

Total_Swap = swap_memory.total / (1024 ** 3)
Used_Swap = swap_memory.used / (1024 ** 3)
Swap_Percent = swap_memory.percent

swap = {
    "total": Total_Swap,
    "used": Used_Swap,
    "percent": Swap_Percent
}

print(ram, swap)