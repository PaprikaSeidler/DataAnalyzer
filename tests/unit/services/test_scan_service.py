import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
from scanners.ipv4_scanner import IPv4Scanner
from scanners.ipv6_scanner import IPv6Scanner
from services.scan_service import ScanService

def test_returns_data_from_one_scanner(tmp_path):
    """Test that the ScanService returns data from one scanner."""

    scanner = IPv4Scanner()
    service = ScanService([scanner])

    content = "Here are some IP addresses: 172.16.0.1, 999.999.999.999, ::1"
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = service.scan_all(str(scan_file))
    assert result == ["172.16.0.1"]

def test_returns_data_from_multiple_scanners(tmp_path):

    scanner1 = IPv4Scanner()
    scanner2 = IPv6Scanner()
    service = ScanService(scanners=[IPv4Scanner(), IPv6Scanner()])

    content = "Here are some IP addresses: 172.16.0.1, 999.999.999.999, ::1"
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = service.scan_all(str(scan_file))
    assert result == ["172.16.0.1", "::1"]

def test_no_results_recieved_from_scanners(tmp_path):
    """Test that the ScanService returns an empty list when no scanners find valid data."""

    scanner1 = IPv4Scanner()
    scanner2 = IPv6Scanner()
    service = ScanService(scanners=[scanner1, scanner2])

    content = "This file contains no valid IP addresses."
    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(content)

    result = service.scan_all(str(scan_file))
    assert result == []