# DataAnalyzer

A CLI tool that scans text files for security-relevant findings and turns them into prioritized incidents — not just a list of matches.

**Status: work in progress.** Scanning is done and tested. A rule engine for severity and incidents is next.

## What it does

Scans a file for IPv4/IPv6 addresses. Every regex match is validated through Python's `ipaddress` module, not trusted on its own — regex finds candidates, a real parser decides what's actually valid.

\```bash
cd src
python main.py scan ../ScanThisFile.txt
\```

## How it's built

\```
interfaces/  → IScanner contract
scanners/    → BaseScanner (shared file logic) + IPv4/IPv6 implementations
services/    → ScanService runs any registered scanner over a file
\```

New detection types plug in without touching existing code — a scanner only implements `_scan(content)`.

## Tests

\```bash
pip install pytest
python -m pytest
\```

Unit + integration tests, run automatically on every push/PR via GitHub Actions.

## Next up

A rule engine that evaluates scan results for relevance and severity (e.g. an unusually high number of IPs in one file, or a known-suspicious IP in a log), turning raw findings into incidents worth actually looking at. Docker support planned after that.
