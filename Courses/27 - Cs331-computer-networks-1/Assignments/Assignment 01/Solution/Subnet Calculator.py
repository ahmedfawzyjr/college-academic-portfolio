import ipaddress

def calculate_subnet(ip_str: str):
    net = ipaddress.ip_network(ip_str, strict=False)
    return {
        "network_address": str(net.network_address),
        "broadcast_address": str(net.broadcast_address),
        "netmask": str(net.netmask),
        "num_hosts": net.num_addresses - 2
    }

if __name__ == "__main__":
    res = calculate_subnet("192.168.1.50/24")
    print("Subnet Calculations:", res)
