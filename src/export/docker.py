"DOC"

import os
import shutil

from utils.logging import Logger
from .exporter import Exporter

class DockerComposeExporter(Exporter):
    "DOC"
    def __init__(self, export_dir, containers_directory):
        self._export_dir = export_dir
        self._containers_directory = containers_directory

    def export_containers(self, logger: Logger):
        "DOC"
        containers = os.listdir(self._containers_directory)
        os.makedirs(f"{self._export_dir}/Docker", exist_ok=True)
        for container in containers:
            if os.path.exists(f"{self._export_dir}/Docker/{container}.zip"):
                os.remove(f"{self._export_dir}/Docker/{container}.zip")

            shutil.make_archive(f"{self._export_dir}/Docker/{container}", 'zip', self._containers_directory+"/"+container)
            logger.write_log(f"Export del container {container} completato.\n")
