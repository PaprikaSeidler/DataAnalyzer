from abc import ABC, abstractmethod

class IScanner(ABC):
    @abstractmethod
    def scan(self, data):
        pass