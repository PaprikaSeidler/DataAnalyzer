import subprocess
import sys

def test_scan_pipeline_finds_ip_addresses(tmp_path):
    """Test the scan pipeline end-to-end using the CLI."""

    scan_file = tmp_path / "scan.txt"
    content = "Here are some IP addresses: 159.116.1.10, 2001:db8::1, ::1"
    scan_file.write_text(content)

    result = subprocess.run([
        sys.executable,
        "src/main.py",
        "scan",
        str(scan_file)
    ],
    capture_output=True,
    text=True
    )  

    assert result.returncode == 0
    assert "159.116.1.10" in result.stdout
    assert "2001:db8::1" in result.stdout
    assert "::1" in result.stdout