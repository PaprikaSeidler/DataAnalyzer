import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
from models.rule import Rule, Severity


def test_rule_stores_values():
    rule = Rule(
        "Test Rule",
        "A test rule",
        Severity.LOW,
        {"key": "value"}
    )

    assert rule.name == "Test Rule"
    assert rule.description == "A test rule"
    assert rule.severity == Severity.LOW
    assert rule.config == {"key": "value"}

def test_severity_enum():
    assert Severity.LOW.value == "low"
    assert Severity.MEDIUM.value == "medium"
    assert Severity.HIGH.value == "high"

def test_rule_severity_type():
    rule = Rule(
        "Test Rule",
        "A test rule",
        Severity.MEDIUM,
        {"key": "value"}
    )
    assert isinstance(rule.severity, Severity)

def test_rule_severity_invalid():
    try:
        rule = Rule(
            "Test Rule",
            "A test rule",
            "invalid_severity",  # This should raise an error
            {"key": "value"}
        )
    except ValueError as e:
        assert str(e) == "'invalid_severity' is not a valid Severity"