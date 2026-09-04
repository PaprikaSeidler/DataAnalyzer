import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from scanners.ipv6_scanner import IPv6Scanner


def test_returns_valid_ipv6_addresses(tmp_path):
    """Test that the IPv6 scanner returns valid IPv6 addresses."""
    scanner = IPv6Scanner()
    content = "Here are some IP addresses: 41a3:5d52:1740:3a2f:bf48:7b0e:8678:0a54, ::1, fe80::1"   
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = scanner.scan(str(scan_file))
    assert result == ["41a3:5d52:1740:3a2f:bf48:7b0e:8678:0a54", "::1", "fe80::1"]

def test_invalid_ipv6_addresses_are_ignored(tmp_path): 
    """Test that invalid IPv6 addresses are ignored."""
    scanner = IPv6Scanner()
    content = "Invalid IPs: 3ffe:1900:4545:3:200:f8ff:fe21, :1"
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = scanner.scan(str(scan_file))
    assert result == []

def test_no_ipv6_addresses_found(tmp_path):
    """Test that no IPv6 addresses are found in a file with no IPs."""
    scanner = IPv6Scanner()
    content = "This file contains no IP addresses."
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = scanner.scan(str(scan_file))
    assert result == []

def test_only_ipv6_addresses(tmp_path):
    """Test that the scanner correctly identifies only IPv6 addresses - no other text or IPv4"""
    scanner = IPv6Scanner()
    content = "Only IPv6s: 41a3:5d52:1740:3a2f:bf48:7b0e:8678:0a54, ::1, fe80::1. Not IPv4: 192.168.1.1, 10.0.0.1, 172.16.0.1"
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)   

    result = scanner.scan(str(scan_file))
    assert result == ["41a3:5d52:1740:3a2f:bf48:7b0e:8678:0a54", "::1", "fe80::1"]

