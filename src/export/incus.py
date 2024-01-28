"""DOC"""

import sys
import os
import subprocess

from utils import logging
from .exporter import Exporter

class IncusExporter(Exporter):
    """DOC"""
    def __init__(self, export_dir):
        self._containers = subprocess.check_output("incus list --format csv --columns=n",
                                                shell=True, text=True).split("\n")
        self._containers.pop()
        self._export_dir = export_dir

    def export_containers(self, logger: logging.Logger):
        """DOC"""
        try:
            os.makedirs(f"{self._export_dir}/Incus", exist_ok=True)
        except FileExistsError:
            pass

        for container in self._containers:
            if os.system(f"incus export {container} {self._export_dir}/Incus/{container}.tar.gz"):
                logger.write_log(f"Backup del container {container} fallito.\n")
                sys.exit(-1)
            else:
                logger.write_log(f"Backup del container {container} completato con successo!\n")
