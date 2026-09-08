import os
import sys
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
import cli
from cli import build_parser

# tests for the scan command
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

# tests for the evaluate command
def test_evaluate_command_accepts_valid_arguments():
    parser = build_parser()

    args = parser.parse_args([
        "evaluate",
        "SuspiciousIP",
        "scan.txt"
    ])

    assert args.command == "evaluate"
    assert args.rule == "SuspiciousIP"
    assert args.file_path == "scan.txt"

def test_evaluate_command_requires_file_path():
    """Test that the evaluate command requires a file path argument."""
    parser = build_parser()

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(["evaluate", "SuspiciousIP"])
    assert excinfo.value.code == 2

def test_evaluate_rule_prints_matches(monkeypatch, capsys):
    """Test that evaluate prints matches returned by the evaluator."""
    class Rule:
        config = {"suspicious_ips": ["203.0.113.10"]}

    class ScannerService:
        def scan_all(self, file_path):
            return ["203.0.113.10"]

    monkeypatch.setattr(cli, "get_rule", lambda rule_name: Rule())
    monkeypatch.setattr(cli, "create_scan_service", lambda: ScannerService())

    args = build_parser().parse_args(["evaluate", "SuspiciousIP", "scan.txt"])
    cli.evaluate_rule(args)

    assert "Matches found: ['203.0.113.10']" in capsys.readouterr().out

def test_evaluate_rule_reports_unknown_rule(monkeypatch, capsys):
    """Test that evaluate reports an unknown rule."""
    def get_unknown_rule(rule_name):
        raise StopIteration

    monkeypatch.setattr(cli, "get_rule", get_unknown_rule)

    args = build_parser().parse_args(["evaluate", "UnknownRule", "scan.txt"])
    cli.evaluate_rule(args)

    assert "Rule not found: UnknownRule" in capsys.readouterr().out

