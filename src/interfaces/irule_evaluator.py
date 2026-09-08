from abc import ABC, abstractmethod

class IRuleEvaluator(ABC):
    @abstractmethod
    def evaluate_rule(self, rule, data):
        pass