import argparse
import scanner

# define the functions here:
def scan(args):
    print("Scanning...")
    findings = scanner.scan_files(args.file_path) 
    print(f"Valid IP addresses found: {findings}")
    print("Scan complete.")

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

