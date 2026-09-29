# PROJECT 001: CHAOS — The Digital Observatory

The beginning of my personal laboratory.

CHAOS is a long-term project focused on observation, computation, experimentation, and the development of systems that can understand and interact with the world around them.

## Current Stage — V0.7

The first stage of CHAOS began with something simple:

**observing the computer it is running on.**

CHAOS then evolved from simply observing information to **organizing and storing what it observes**.

The next step was **retrieving and analyzing historical observations**.

CHAOS has now taken another major step:

**integrating its observation systems into a single Digital Observatory capable of detecting events in the environment it observes.**

The project has expanded from individual observation modules into a system where multiple sources of information can be collected, combined, stored, analyzed, and interpreted through deterministic rules.

The current conceptual flow is:

```text
Observe → Store → Retrieve → Analyze → Detect
```

This is the foundation upon which future CHAOS systems will be built.

### Current Systems

**CPU Observation**

* CPU usage
* CPU frequency
* Physical CPU cores
* Logical CPU cores

The CPU observation system uses a function that collects fresh CPU information whenever it is called, allowing CHAOS to observe the computer dynamically.

**GPU Observation**

CHAOS can now observe AMD GPU information through AMD ADLX.

Current GPU observations include:

* GPU name
* GPU usage
* GPU temperature
* GPU clock speed
* VRAM usage
* GPU power consumption
* GPU fan speed

This allows CHAOS to observe not only the general computer system, but also the dedicated graphics processor.

**Disk Observation**

* Disk device
* Mount point
* Filesystem
* Total storage
* Used storage
* Free storage
* Storage usage percentage

CHAOS can observe multiple storage devices and evaluate their current state.

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

**Process Observation**

CHAOS can now observe currently running processes.

Process observations include:

* Process ID
* Process name
* Process status
* CPU usage
* Memory usage

This allows CHAOS to observe not only the hardware itself, but also what is actively running on the system.

**Network Observation**

CHAOS can observe the computer's network interfaces and their current state.

Current network observations include:

* Interface name
* Network addresses
* Address family
* Bytes sent
* Bytes received
* Packets sent
* Packets received

This extends CHAOS's observation capabilities beyond the local hardware and into the communication layer of the system.

## Data System

The Data layer is responsible for receiving, organizing, storing, and retrieving information collected by CHAOS.

Currently, it uses:

* Python dictionaries for structured data
* SQLite for persistent storage
* SQL tables for organizing collected information
* SQL queries for retrieving stored observations
* Parameterized queries for dynamic filtering
* JSON serialization for storing complete observations

CHAOS can now store a complete observation containing information from multiple observation systems.

The current data flow is:

```text
                    CHAOS
                      │
                      ▼
                  Observation
                      │
        ┌─────────────┼─────────────┐
        │             │             │
       Core        Processes      Network
        │
        ├── CPU
        ├── GPU
        ├── Disk
        ├── Memory
        └── System
                      │
                      ▼
                    Data
                      │
                      ▼
                   SQLite
                      │
                      ▼
                 Historical Data
```

Previously, CHAOS primarily stored CPU observations.

It can now store a broader representation of the state of the computer.

This represents an important transition from:

```text
Individual Observation
```

to:

```text
Complete System Observation
```

## CHAOS Orchestrator

The `CHAOS` layer now acts as the central orchestration layer for the observatory.

The `observe()` function collects information from the different observation systems and combines them into a single observation.

Conceptually:

```text
CPU ───────┐
GPU ───────┤
Disk ──────┤
Memory ────┤
System ────┤
Processes ─┤──→ CHAOS.observe()
Network ───┘          │
                      ▼
                Complete Observation
```

This allows CHAOS to operate as a single system rather than as a collection of unrelated modules.

## Event Detection

CHAOS has now begun detecting events from its observations.

The first event detector monitors disk usage.

When a disk reaches or exceeds the configured threshold, CHAOS generates an event.

For example:

```text
C:\ → 92.0% usage
        │
        ▼
   Threshold: 90%
        │
        ▼
   Event detected
```

The resulting event contains:

* Event type
* Event source
* Human-readable message
* Relevant observation data

Example:

```python
{
    "type": "disk_high_usage",
    "source": "Disk",
    "message": "C:\\ is using 92.0% of its capacity.",
    "data": {...}
}
```

This represents the beginning of a transition from:

```text
Observation → Storage
```

toward:

```text
Observation → Analysis → Detection
```

CHAOS is no longer only recording what exists.

It has begun recognizing when something important happens.

## Data Analysis

CHAOS has begun its first basic analysis operations.

The current data system can calculate the average CPU usage of a collection of historical observations.

For example:

```text
22.8%
13.5%
35.9%
44.0%
21.8%
```

can produce:

```text
Average CPU usage: 27.6%
```

This represents the beginning of the analytical foundation of CHAOS.

The long-term goal is to expand analysis beyond simple averages into:

* Trends
* Threshold detection
* Anomaly detection
* Historical comparisons
* Correlations
* Pattern recognition

These systems will initially be deterministic and computational rather than AI-driven.

## Continuous Observation

CHAOS includes a scheduler capable of collecting CPU observations at regular intervals.

The current CPU observation interval is:

```text
10 minutes
```

This creates a growing historical record of CPU activity.

Continuous observation will eventually be expanded to the complete CHAOS observation cycle.

## Current Architecture

The current architecture is:

```text
PROJECT-001-CHAOS/

├── Core/
│   ├── __init__.py
│   ├── cpu.py
│   ├── disk.py
│   ├── memory.py
│   ├── system.py
│   └── gpu.py
│
├── Data/
│   ├── __init__.py
│   ├── data.py
│   └── database.py
│
├── Events/
│   ├── __init__.py
│   └── events.py
│
├── Network/
│   ├── __init__.py
│   └── network.py
│
├── Processes/
│   ├── __init__.py
│   └── processes.py
│
├── CHAOS/
│   ├── __init__.py
│   └── chaos.py
│
├── .gitignore
└── README.md
```

Runtime data such as `data.db` and Python-generated cache files are excluded from the source repository.

## Technologies

* Python
* psutil
* SQLite
* sqlite3
* schedule
* platform
* time
* JSON
* AMD ADLX

## Current Conceptual Model

CHAOS is gradually being built around the following loop:

```text
Observe
   ↓
Store
   ↓
Retrieve
   ↓
Analyze
   ↓
Detect
   ↓
Improve
   ↓
Observe Again
```

The current system is still deterministic.

It does not yet attempt to understand the world through artificial intelligence.

Instead, the objective is to first build a real observatory capable of collecting reliable information and developing a history of what it observes.

AI and more advanced reasoning