import os
import sys
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
from repository.rule_repo import RuleRepository
from models.rule import Rule,Severity

@pytest.fixture
def rule_repo(tmp_path):
    """Fixture to create a RuleRepository instance with a temporary file."""
    temp_file = tmp_path / "rules.json"
    return RuleRepository(file_path=str(temp_file))

def test_add_rule(rule_repo):
    """Test adding a rule to the repository."""
    
    rule = Rule("Test Rule", "A test rule", Severity.LOW, {"key": "value"})
    rule_repo.add_rule(rule)
    assert len(rule_repo.get_rules()) == 1
    assert rule_repo.get_rules()[0].name == "Test Rule"
    assert rule_repo.get_rules()[0].description == "A test rule"
    assert rule_repo.get_rules()[0].severity == Severity.LOW
    assert rule_repo.get_rules()[0].config == {"key": "value"}

def test_remove_rule(rule_repo):
    """Test removing a rule from the repository."""
    rule = Rule("Test Rule", "A test rule", Severity.LOW, {"key": "value"})
    rule_repo.add_rule(rule)
    rule_repo.remove_rule(rule)
    assert len(rule_repo.get_rules()) == 0

def test_remove_nonexistent_rule(rule_repo):
    """Test removing a rule that does not exist in the repository."""
    rule = Rule("Nonexistent Rule", "This rule does not exist", Severity.HIGH, {"key": "value"})
    with pytest.raises(ValueError):
        rule_repo.remove_rule(rule)

def test_add_non_rule_instance(rule_repo):
    """Test adding a non-Rule instance to the repository."""
    with pytest.raises(ValueError):
        rule_repo.add_rule("This is not a Rule")