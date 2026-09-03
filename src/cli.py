import argparse
from scanners.ipv4_scanner import IPv4Scanner
from scanners.ipv6_scanner import IPv6Scanner
from services import scan_service


# define the functions here:
def scan(args):
    scanners = scan_service.ScanService(scanners=
                             [IPv4Scanner(), IPv6Scanner()])
    try:
        results = scanners.scan_all(args.file_path)
        if results:
            print(f"Valid IP addresses found: {results}")
        else:
            print("No valid IP addresses found.")
    except FileNotFoundError:
        print(f"File not found: {args.file_path}")
        return
    except Exception as e:
        print(f"An error occurred while scanning: {e}")


# add functions for command line arguments here.
# this ensures the functions can be called from the command line interface.
def build_parser():
    parser = argparse.ArgumentParser(prog="data_analyzer", description="Data Analyzer CLI")
    subparsers = parser.add_subparsers(
        dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan data")
    scan_parser.set_defaults(func=scan)
    scan_parser.add_argument("file_path", type=str, help="Path to the file to scan")

    return parser

