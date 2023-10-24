"""DOC"""

from abc import ABC, abstractmethod

from utils import logging

class Exporter(ABC):
    """DOC"""
    @abstractmethod
    def export_containers(self, logger: logging.Logger):
        """DOC"""
