from adlx import ADLX


def get_gpu():
    helper = ADLX.ADLXHelper()
    result = helper.Initialize()

    if result != ADLX.ADLX_RESULT.ADLX_OK:
        raise RuntimeError(f"ADLX initialization failed: {result}")

    system = helper.GetSystemServices()
    gpus = system.GetGPUs()
    monitoring = system.GetPerformanceMonitoringServices()

    GPU = []

    for gpu in gpus:
        metrics = monitoring.GetCurrentGPUMetrics(gpu)

        GPU.append({
            "name": gpu.Name(),
            "usage": metrics.GPUUsage(),
            "temperature": metrics.GPUTemperature(),
            "clock": metrics.GPUClockSpeed(),
            "vram": metrics.GPUVRAM(),
            "power": metrics.GPUPower(),
            "fan": metrics.GPUFanSpeed()
        })

        del metrics

    del monitoring
    del gpu
    del gpus
    del system

    helper.Terminate()
    del helper

    return GPU


print(get_gpu())