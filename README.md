# PROJECT 001: CHAOS — The Digital Observatory

The beginning of my personal laboratory.

CHAOS is a long-term project focused on observation, computation, experimentation, and the development of systems that can understand and interact with the world around them.

## Current Stage — V0.2

The first stage of CHAOS begins with something simple:

**observing the computer it is running on.**

The current Python modules use `psutil` to collect information about the computer's hardware and system resources.

### Current Systems

**CPU Observation**

* CPU usage
* CPU frequency
* Physical CPU cores
* Logical CPU cores

**Disk Observation**

* Disk device
* Mount point
* Filesystem
* Total storage
* Used storage
* Free storage
* Storage usage percentage

**Memory Observation**

* Total RAM
* Available RAM
* Used RAM
* RAM usage percentage
* Total swap memory
* Used swap memory
* Swap usage percentage

**System Observation**

* Operating system
* System node
* System release
* Machine architecture
* Python version
* Boot time
* System uptime

The collected information is organized into Python data structures and displayed as structured data.

## Example

```python
cpu = {
    "usage": usage,
    "frequency": freq.current,
    "physical_cores": physical_cores,
    "logical_cores": logical_cores
}
```

This is the foundation of the observation system of CHAOS.

## Technologies

* Python
* psutil
* platform
* time

## Project Structure

```text
PROJECT 001 CHAOS/
│
├── Core/
│   ├── cpu.py
│   ├── disk.py
│   ├── memory.py
│   └── system.py
│
└── README.md
```

## Project Status

🚧 Early development

**Version:** V0.2

**Core systems:** CPU Observation + Disk Observation + Memory Observation + System Observation

The Core observation stage is complete.

CHAOS will evolve gradually as new observation, experimentation, and computational systems are developed.
