"""DOC"""

import sys
import os
import subprocess

from utils import logging
from .exporter import Exporter

class LxdExporter(Exporter):
    """DOC"""
    def __init__(self, export_dir):
        self._containers = subprocess.check_output("lxc list --format csv --columns=n",
                                                shell=True, text=True).split("\n")
        self._containers.pop()
        self._export_dir = export_dir

    def export_containers(self, logger: logging.Logger):
        """DOC"""
        try:
            os.makedirs(f"{self._export_dir}/LXD", exist_ok=True)
        except FileExistsError:
            pass

        for container in self._containers:
            if os.system(f"lxc export {container} {self._export_dir}/LXD/{container}.tar.gz"):
                logger.write_log(f"Backup del container {container} fallito.\n")
                sys.exit(-1)
            else:
                logger.write_log(f"Backup del container {container} completato con successo!\n")
