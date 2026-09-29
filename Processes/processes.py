import psutil  # Imports psutil so CHAOS can observe running processes.


def get_processes():  # Defines the function that collects running-process information.
    processes = []  # Creates a list where CHAOS will store the observations.

    for process in psutil.process_iter(["pid", "name", "status", "cpu_percent", "memory_percent"]):  # Goes through the processes currently running on the computer.
        processes.append(process.info)  # Adds the information collected from the current process to the list.

    return processes  # Returns all observed processes to CHAOS.


if __name__ == "__main__":  # Runs the test below only when this file is executed directly.
    processes = get_processes()  # Collects the currently running processes.

    for process in processes[:10]:  # Displays the first ten processes as a simple test.
        print(process)  # Prints the information collected for the current process.