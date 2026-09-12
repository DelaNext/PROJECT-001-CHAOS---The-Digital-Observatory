import psutil

Disks = []
for partition in psutil.disk_partitions():

    usage = psutil.disk_usage(partition.mountpoint)

    Device = partition.device
    Mountpoint = partition.mountpoint
    Filesystem = partition.fstype
    Total = usage.total / (1024 ** 3)
    Used = usage.used / (1024 ** 3)
    Free = usage.free / (1024 ** 3)
    Percent = usage.percent

    Disk = {
    "Device": Device,
    "Mountpoint": Mountpoint,
    "Filesystem": Filesystem,
    "Total": Total,
    "Used": Used,
    "Free": Free,
    "Percent": Percent
           }

    Disks.append(Disk)

print(Disks)