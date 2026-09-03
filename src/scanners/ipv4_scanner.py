from interfaces.iscanner import IScanner
import re
import ipaddress

class IPv4Scanner(IScanner):
    def scan(self, data):
        # Implement the scanning logic for IPv4 addresses here
        
        with open(data, 'r') as f:
            content = f.read()

            ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
            matches = re.findall(ipv4_pattern, content)
            valid_ipv4_addresses = []

            for ip in matches:
                try:
                    parsed_ip = ipaddress.ip_address(ip)
                    if parsed_ip.version == 4:
                        valid_ipv4_addresses.append(ip)
                except ValueError:
                    pass # skip invalid IP addresses

            return valid_ipv4_addresses