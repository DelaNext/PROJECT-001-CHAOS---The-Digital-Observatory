from adlx import ADLX  # Imports AMD's ADLX library so Python can communicate with the GPU.


def get_gpu():  # Defines the function that collects information about the GPU.
    helper = ADLX.ADLXHelper()  # Creates the ADLX helper used to communicate with AMD hardware.
    result = helper.Initialize()  # Initializes ADLX.

    if result != ADLX.ADLX_RESULT.ADLX_OK:  # Checks whether ADLX initialized successfully.
        raise RuntimeError(f"ADLX initialization failed: {result}")  # Stops the program if initialization failed.

    system = helper.GetSystemServices()  # Gets ADLX system services.
    gpus = system.GetGPUs()  # Gets the GPUs detected by the computer.
    monitoring = system.GetPerformanceMonitoringServices()  # Gets the GPU performance-monitoring service.

    GPU = []  # Creates a list to store information about all detected GPUs.

    for gpu in gpus:  # Goes through every GPU detected by the system.
        metrics = monitoring.GetCurrentGPUMetrics(gpu)  # Gets the current performance measurements for this GPU.

        GPU.append({  # Adds this GPU's information to our result list.
            "name": gpu.Name(),  # Gets the GPU's name.
            "usage": metrics.GPUUsage(),  # Gets current GPU utilization as a percentage.
            "temperature": metrics.GPUTemperature(),  # Gets current GPU temperature in Celsius.
            "clock": metrics.GPUClockSpeed(),  # Gets current GPU clock speed in MHz.
            "vram": metrics.GPUVRAM(),  # Gets current VRAM usage in MB.
            "power": metrics.GPUPower(),  # Gets current GPU power consumption in watts.
            "fan": metrics.GPUFanSpeed()  # Gets current GPU fan speed in RPM.
        })

        del metrics  # Releases the metrics interface before ADLX is terminated.

    del monitoring  # Releases the performance-monitoring interface.
    del gpu  # Releases the GPU interface.
    del gpus  # Releases the GPU collection.
    del system  # Releases the system interface.

    helper.Terminate()  # Terminates ADLX after all interfaces have been released.
    del helper  # Releases the ADLX helper.

    return GPU  # Returns the collected GPU information.


print(get_gpu())  # Runs the GPU observation and prints the result.