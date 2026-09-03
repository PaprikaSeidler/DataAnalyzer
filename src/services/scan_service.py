class ScanService:
    def __init__(self, scanners):
        self.scanners = scanners

    def scan_all(self, data):
        results = []
        for scanner in self.scanners:
            results.extend(scanner.scan(data))
        return results