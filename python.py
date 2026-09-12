
import psutil


usage = psutil.cpu_percent(interval=0.5)
freq = psutil.cpu_freq()
physical_cores =psutil.cpu_count(logical=False)
logical_cores =psutil.cpu_count(logical=True)

cpu = {
    "usage": usage,
    "frequency": freq.current,
    "physical_cores": physical_cores,
    "logical_cores": logical_cores
}

print(cpu)