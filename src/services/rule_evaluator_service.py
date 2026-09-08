class RuleEvaluatorService:
    def __init__(self, rule_evaluator):
        self.rule_evaluator = rule_evaluator

    def evaluate_rule(self, rule, data):
        return self.rule_evaluator.evaluate_rule(rule, data)

    def evaluate_rules(self, rules, data):
        results = []
        for rule in rules:
            result = self.evaluate_rule(rule, data)
            results.append(result)
        return results