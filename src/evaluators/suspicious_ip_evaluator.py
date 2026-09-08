from evaluators.base_evaluator import BaseEvaluator

class SuspiciousIPEvaluator(BaseEvaluator):
    def _evaluate(self, config, matches):
        suspicious_ips = config.get("suspicious_ips", [])

        return [
            ip for ip in matches
            if ip in suspicious_ips
        ]