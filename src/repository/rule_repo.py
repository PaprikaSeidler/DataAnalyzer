import json
from models.rule import Rule, Severity

class RuleRepository:
    def __init__(self, file_path="rules.json"):
        self.file_path = file_path
        self.rules = []
        self._load_rules()

    def _load_rules(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                saved_rules = json.load(file)
        except FileNotFoundError:
            return

        self.rules = [
            Rule(
                name=item["name"],
                description=item["description"],
                severity=Severity(item["severity"]),
                config=item["config"]
            )
            for item in saved_rules
        ]

    def _save_rules(self):
        saved_rules = [
            {
                "name": rule.name,
                "description": rule.description,
                "severity": rule.severity.value,
                "config": rule.config
            }
            for rule in self.rules
        ]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(saved_rules, file, indent=4)

    def add_rule(self, rule):
        if isinstance(rule, Rule):
            self.rules.append(rule)
            self._save_rules()
        else:
            raise ValueError("Only instances of Rule can be added.")

    def remove_rule(self, rule):
        if rule in self.rules:
            self.rules.remove(rule)
            self._save_rules()
        else:
            raise ValueError("Rule not found in the repository.")

    def get_rules(self):
        return self.rules

if __name__ == "__main__":
    repo = RuleRepository()
    rule1 = Rule("SuspiciousIP", "Detects known suspicious IP addresses", Severity.HIGH, {
            "suspicious_ips": [
                "203.0.113.10",
                "198.51.100.25"
            ]
        })
    repo.add_rule(rule1)

