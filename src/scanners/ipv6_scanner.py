import ipaddress
import re
from scanners.base_scanner import BaseScanner

class IPv6Scanner(BaseScanner):
    def _scan(self, content):
        ipv6_pattern = r'\b(?:[A-Fa-f0-9]{1,4}:){1,7}(?::[A-Fa-f0-9]{1,4}){1,7}\b|\b(?:[A-Fa-f0-9]{1,4}:){2,7}[A-Fa-f0-9]{1,4}\b|::(?:[A-Fa-f0-9]{1,4}:?){0,7}[A-Fa-f0-9]{0,4}\b'
        matches = re.findall(ipv6_pattern, content)
        valid_ipv6_addresses = []

        for ip in matches:
            try:
                parsed_ip = ipaddress.ip_address(ip)
                if parsed_ip.version == 6:
                    valid_ipv6_addresses.append(ip)
            except ValueError:
                pass 

        return valid_ipv6_addresses