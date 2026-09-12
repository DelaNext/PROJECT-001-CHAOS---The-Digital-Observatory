# PROJECT 001: CHAOS — The Digital Observatory

The beginning of my personal laboratory.

CHAOS is a long-term project focused on observation, computation, experimentation, and the development of systems that can understand and interact with the world around them.

## Current Stage — V0.1

The first version of CHAOS begins with something simple:

**observing the computer it is running on.**

The current Python module uses `psutil` to collect basic CPU information:

* CPU usage
* CPU frequency
* Physical CPU cores
* Logical CPU cores

The collected information is organized into a Python dictionary and displayed as structured data.

## Example

```python
cpu = {
    "usage": usage,
    "frequency": freq.current,
    "physical_cores": physical_cores,
    "logical_cores": logical_cores
}
```

This is the first observation system of CHAOS.

## Technologies

* Python
* psutil

## Project Status

🚧 Early development

**Version:** V0.1
**Current system:** CPU Observation

This project will evolve gradually as new observation and experimental systems are developed.
