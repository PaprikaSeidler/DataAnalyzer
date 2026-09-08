import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[3] / "src"))

from services.rule_evaluator_service import RuleEvaluatorService


class FakeEvaluator:
    def evaluate_rule(self, rule, data):
        return [item for item in data if item == rule]


def test_evaluate_rules_returns_results():
    '''Test that the RuleEvaluatorService correctly evaluates multiple rules and returns the expected results.'''
    service = RuleEvaluatorService(FakeEvaluator())

    result = service.evaluate_rules(
        rules=["suspicious-ip"],
        data=["suspicious-ip", "normal-ip"],
    )

    assert result == [["suspicious-ip"]]

def test_evaluate_rule_returns_results():
    '''Test that the RuleEvaluatorService correctly evaluates a single rule and returns the expected results.'''
    service = RuleEvaluatorService(FakeEvaluator())

    result = service.evaluate_rule(
        rule="suspicious-ip",
        data=["suspicious-ip", "normal-ip"],
    )

    assert result == ["suspicious-ip"]

def test_evaluate_rules_with_no_matches():
    '''Test that the RuleEvaluatorService returns empty results when no matches are found.'''
    service = RuleEvaluatorService(FakeEvaluator())

    result = service.evaluate_rules(
        rules=["suspicious-ip"],
        data=["normal-ip"],
    )

    assert result == [[]]

    