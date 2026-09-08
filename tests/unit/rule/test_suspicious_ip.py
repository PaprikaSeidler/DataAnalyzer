import pytest
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
from evaluators.suspicious_ip_evaluator import SuspiciousIPEvaluator
from models.rule import Rule, Severity


def create_suspicious_ip_rule():
	'''Test helper function to create a SuspiciousIP rule for testing purposes.'''
	return Rule(
		"SuspiciousIP",
		"Detects known suspicious IP addresses",
		Severity.HIGH,
		{"suspicious_ips": ["203.0.113.10"]}
	)


def test_returns_suspicious_ip_matches():
	'''Test that the evaluator correctly identifies suspicious IP addresses.'''
	evaluator = SuspiciousIPEvaluator()

	result = evaluator.evaluate_rule(
		create_suspicious_ip_rule(),
		["203.0.113.10", "192.168.1.1"]
	)

	assert result == ["203.0.113.10"]


def test_returns_empty_for_no_matches():
	'''Test that the evaluator returns an empty list when there are no matches.'''
	evaluator = SuspiciousIPEvaluator()

	result = evaluator.evaluate_rule(
		create_suspicious_ip_rule(),
		["192.168.1.1", "10.0.0.1"]
	)

	assert result == []


def test_ignores_non_suspicious_ips():
	'''Test that the evaluator ignores non-suspicious IP addresses.'''
	evaluator = SuspiciousIPEvaluator()

	result = evaluator.evaluate_rule(
		create_suspicious_ip_rule(),
		["192.168.1.1"]
	)

	assert result == []


