# DataAnalyzer

DataAnalyzer is a small command-line security analysis tool that scans text files for IP addresses and evaluates the results against configurable rules.

The goal is to go beyond simply detecting data: rules determine whether something is relevant and assign a severity, laying the groundwork for turning rule matches into prioritized incidents.

> **Status: Work in Progress**
>
> The core scanning, rule configuration, rule evaluation, testing, and CI are implemented. Incident generation and additional analysis rules are currently being developed.

## Features

- IPv4 and IPv6 scanning and validation
- Configurable analysis rules stored in JSON
- Severity levels stored per rule (basis for future incident prioritization)
- Rule evaluation that turns scan results into rule matches
- Unit and integration tests
- Automated testing with GitHub Actions

## Architecture

The application follows a simple pipeline:

```text
Text file
   ↓
Scanners
   ↓
Scan results
   ↓
Rules
   ↓
Matches
   ↓
Incidents (planned)
```

Scanners are responsible for detecting data, while rules determine whether detected data represents something worth investigating. This keeps detection and analysis separate and makes it possible to add new rules without modifying the scanners.

Rule matches are currently the end result of a scan. Turning matches into severity-ranked incidents is the next step on the roadmap.

## Current Rules

### SuspiciousIP

Detects IP addresses from a configurable list of known suspicious addresses.

**Severity:** High

## Running the application

From the project root:

```bash
python src/main.py scan ScanThisFile.txt
```

To evaluate a file against a specific rule:

```bash
python src/main.py evaluate SuspiciousIP ScanThisFile.txt
```

## Running the tests

```bash
pip install pytest
python -m pytest
```

Tests are also run automatically through GitHub Actions on pushes and pull requests.

## Roadmap

The project is intentionally being developed incrementally. Planned improvements include:

- Incident generation from rule matches
- Additional analysis rules e.g. TooManyIPsInFile
- Improved incident reporting
- Persistent scan history
- Correlation of incidents across multiple scans
- Additional scanners and data types
- Docker support for easier setup and deployment
- A simple UI for browsing scans and incidents

The focus is on keeping the system small, testable, and easy to reason about rather than adding complexity for its own sake.
