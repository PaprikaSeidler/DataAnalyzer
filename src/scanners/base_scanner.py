from interfaces.iscanner import IScanner
from abc import ABC, abstractmethod

class BaseScanner(IScanner):

    def scan(self, file_path: str):
        with open(file_path, 'r') as f:
            content = f.read()
            return self._scan(content)

    @abstractmethod
    def _scan(self, content: str):
        pass
    