import argparse
from pathlib import Path
from repository.rule_repo import RuleRepository
from scanners.ipv4_scanner import IPv4Scanner
from scanners.ipv6_scanner import IPv6Scanner
from evaluators.suspicious_ip_evaluator import SuspiciousIPEvaluator
from services import scan_service
from services import rule_evaluator_service


def create_scan_service():
    return scan_service.ScanService(
        scanners=[IPv4Scanner(), IPv6Scanner()]
    )


def get_rule(rule_name):
    rules_path = Path(__file__).resolve().parents[1] / "rules.json"
    rules = RuleRepository(str(rules_path)).get_rules()

    return next(rule for rule in rules if rule.name == rule_name)


def scan(args):
    try:
        results = create_scan_service().scan_all(args.file_path)
        if results:
            print(f"Valid IP addresses found: {results}")
        else:
            print("No valid IP addresses found.")
    except FileNotFoundError:
        print(f"File not found: {args.file_path}")
        return
    except Exception as e:
        print(f"An error occurred while scanning: {e}")


def evaluate_rule(args):
    try:
        rule = get_rule(args.rule)
        findings = create_scan_service().scan_all(args.file_path)
        evaluator = rule_evaluator_service.RuleEvaluatorService(
            rule_evaluator=SuspiciousIPEvaluator()
        )
        matches = evaluator.evaluate_rule(rule, findings)

        if matches:
            print(f"Matches found: {matches}")
        else:
            print("No matches found.")

    except StopIteration:
        print(f"Rule not found: {args.rule}")
    except FileNotFoundError:
        print(f"File not found: {args.file_path}")


def build_parser():
    parser = argparse.ArgumentParser(prog="data_analyzer", description="Data Analyzer CLI")
    subparsers = parser.add_subparsers(
        dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan data")
    scan_parser.set_defaults(func=scan)
    scan_parser.add_argument("file_path", type=str, help="Path to the file to scan")

    evaluate_parser = subparsers.add_parser("evaluate", help="Evaluate a rule to find matches")
    evaluate_parser.set_defaults(func=evaluate_rule)
    evaluate_parser.add_argument("rule", type=str)
    evaluate_parser.add_argument("file_path", type=str)

    return parser

