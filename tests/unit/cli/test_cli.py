import os
import sys
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
from cli import build_parser

def test_scan_command_accepts_valid_file_path():
    """Test that the scan command accepts a valid file path argument."""
    parser = build_parser()

    args = parser.parse_args(['scan', 'scan.txt'])

    assert args.command == 'scan'
    assert args.file_path == 'scan.txt'

def test_scan_command_requires_file_path():
    """Test that the scan command requires a file path argument."""
    parser = build_parser()

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(['scan'])
    assert excinfo.value.code == 2 

