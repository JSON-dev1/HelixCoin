# Import requests and regex library
import requests
import re
import socket
import time
 
def get_external_ip():
    # Make a request to checkip.dyndns.org as proposed
    # in https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery#DNS_Addresses
    response = requests.get('http://checkip.dyndns.org').text
 
    # Filter the response with a regex for an IPv4 address
    ip = re.search("(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response).group()
    return ip
 
external_ip = get_external_ip()
print(external_ip)

def get_node_addresses():
    # The list of seeds as hardcoded in a Bitcoin client
    # view https://en.bitcoin.it/wiki/Satoshi_Client_Node_Discovery#DNS_Addresses
    dns_seeds = [
        ("seed.bitcoin.sipa.be", 8333),
        ("dnsseed.bluematt.me", 8333),
        ("dnsseed.bitcoin.dashjr.org", 8333),
        ("seed.bitcoinstats.com", 8333),
        ("seed.bitnodes.io", 8333),
        ("bitseed.xf2.org", 8333),
    ]
 
    # The list where we store our found peers
    found_peers = []
    try:
        # Loop our seed list
        for (ip_address, port) in dns_seeds:
            index = 0
            # Connect to a dns address and get the A records
            for info in socket.getaddrinfo(ip_address, port,
                                           socket.AF_INET, socket.SOCK_STREAM,
                                           socket.IPPROTO_TCP):
                # The IP address and port is at index [4][0]
                # for example: ('13.250.46.106', 8333)
                found_peers.append((info[4][0], info[4][1]))
    except Exception:
        return found_peers
 
peers = get_node_addresses()
print(peers)
