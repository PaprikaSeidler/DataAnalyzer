import subprocess
import sys


def test_evaluator_pipeline_finds_suspicious_ips(tmp_path):
    """Test the evaluator pipeline end-to-end using the CLI.
    flow: fil -> scanner -> regelopslag -> evaluator -> CLI-output"""

    scan_file = tmp_path / "scan.txt"
    scan_file.write_text(
        "IPs: 203.0.113.10, 192.168.1.1, ::1"
    )

    result = subprocess.run(
        [
            sys.executable,
            "src/main.py",
            "evaluate",
            "SuspiciousIP",
            str(scan_file),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "203.0.113.10" in result.stdout
    assert "::1" in result.stdout
    assert "192.168.1.1" not in result.stdout