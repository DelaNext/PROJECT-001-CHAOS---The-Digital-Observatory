def create_event(event_type, source, message, data=None):
    event = {
        "type": event_type,
        "source": source,
        "message": message,
        "data": data,
    }

    return event


if __name__ == "__main__":
    event = create_event(
        "cpu_high",
        "CPU",
        "CPU usage exceeded the configured threshold.",
        {"usage": 95},
    )

    print(event)

def detect_disk_events(disks):
    events = []

    for disk in disks:
        if disk["Percent"] >= 90:
            events.append(create_event(
                "disk_high_usage",
                "Disk",
                f'{disk["Device"]} is using {disk["Percent"]}% of its capacity.',
                disk
            ))

    return events