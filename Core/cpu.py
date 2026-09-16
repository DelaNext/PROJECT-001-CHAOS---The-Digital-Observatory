import psutil

def get_cpu():
    return {
        "usage": psutil.cpu_percent(interval=0.5),
        "frequency": psutil.cpu_freq().current,
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
    }   