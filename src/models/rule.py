from enum import Enum

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Rule:
    def __init__(self, name, description, severity, config):
        self.name = name
        self.description = description
        self.severity = severity
        self.config = config

    