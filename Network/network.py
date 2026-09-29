import psutil


def get_network():
    interfaces = psutil.net_if_addrs()
    statistics = psutil.net_io_counters(pernic=True)

    Network = []

    for name, addresses in interfaces.items():
        interface = {
            "name": name,
            "addresses": [],
        }

        for address in addresses:
            interface["addresses"].append({
                "family": str(address.family),
                "address": address.address,
            })

        if name in statistics:
            stats = statistics[name]

            interface["traffic"] = {
                "bytes_sent": stats.bytes_sent,
                "bytes_received": stats.bytes_recv,
                "packets_sent": stats.packets_sent,
                "packets_received": stats.packets_recv,
            }

        Network.append(interface)

    return Network


if __name__ == "__main__":
    network = get_network()

    for interface in network:
        print(interface)