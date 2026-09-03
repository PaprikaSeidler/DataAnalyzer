import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from scanners.ipv4_scanner import IPv4Scanner

def test_returns_valid_ipv4_addresses(tmp_path):
    """Test that the IPv4 scanner returns valid IPv4 addresses."""
    scanner = IPv4Scanner()
    content = "Here are some IP addresses: 192.168.1.1, 10.0.0.1, 172.16.0.1"
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = scanner.scan(str(scan_file))
    assert result == ["192.168.1.1", "10.0.0.1", "172.16.0.1"]

def test_invalid_ipv4_addresses_are_ignored(tmp_path): 
    """Test that invalid IPv4 addresses are ignored."""
    scanner = IPv4Scanner()
    content = "Invalid IPs: 999.999.999.999, 256.256.256.256, 192.168.1.300"
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = scanner.scan(str(scan_file))
    assert result == []