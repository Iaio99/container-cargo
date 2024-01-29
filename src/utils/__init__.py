"""DOC"""
import os
import shutil

__all__ = ["logging", "notification", "parser", "syncing"]

def remove_exported_containers(export_dir: str):
    """DOC"""
    os.chdir(export_dir)
    containers = os.listdir(export_dir)
    for c in containers:
        try:
            shutil.rmtree(c)
        except NotADirectoryError:
            os.remove(c)