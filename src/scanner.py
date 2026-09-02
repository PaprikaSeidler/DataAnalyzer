import re
import ipaddress

def scan_files(file_path):

    with open(file_path, 'r') as f:
        content = f.read()

    # Use regex to find potential IP addresses in the content. 
    # Both IPv4 and IPv6 addresses are supported.
    regex_matches = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b|(?:[0-9A-Fa-f]{1,4}:){1,7}[0-9A-Fa-f]{1,4}\b', content)
    valid_ips = []

    for ip in regex_matches:
        try:
            parsed_ip = ipaddress.ip_address(ip)
            valid_ips.append(ip)

        except ValueError:
            continue  # Skip invalid IP addresses

    return valid_ips    