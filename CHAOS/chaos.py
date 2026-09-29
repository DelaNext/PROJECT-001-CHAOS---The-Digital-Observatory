from Data.database import store_observation
from Core.cpu import get_cpu
from Core.gpu import get_gpu
from Core.disk import Disks
from Core.memory import ram, swap
from Core.system import System
from Processes.processes import get_processes
from Network.network import get_network
from Events.events import detect_disk_events


def observe():
    observation = {
        "cpu": get_cpu(),
        "gpu": get_gpu(),
        "disk": Disks,
        "memory": ram,
        "swap": swap,
        "system": System,
        "processes": get_processes(),
        "network": get_network(),
    }

    observation["events"] = detect_disk_events(observation["disk"])

    return observation


if __name__ == "__main__":
    observation = observe()

    store_observation(observation)

    print("Observation stored.")

    print("Events detected:", observation["events"])