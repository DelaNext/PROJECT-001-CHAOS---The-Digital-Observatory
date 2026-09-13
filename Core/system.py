import platform
import psutil
import time

boot_time = psutil.boot_time()

System = platform.system()
Node = platform.node()
Release = platform.release()
Machine = platform.machine()
Architecture = platform.architecture()
Python_version = platform.python_version()
Uptime = time.time() - boot_time

System = {
    "name": System,
    "node": Node,
    "release": Release,
    "machine": Machine,
    "architecture": Architecture,
    "python_version": Python_version,
    "boot_time": boot_time,
    "uptime": Uptime
}

print(System)