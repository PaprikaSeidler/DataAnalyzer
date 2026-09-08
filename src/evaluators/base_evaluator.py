from abc import ABC, abstractmethod
from interfaces.irule_evaluator import IRuleEvaluator

class BaseEvaluator(IRuleEvaluator, ABC):
    def evaluate_rule(self, rule, matches):
            return self._evaluate(rule.config, matches)

    @abstractmethod
    def _evaluate(self, config, matches):
        pass
            

