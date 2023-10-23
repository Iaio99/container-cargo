"""DOC"""
import sys
import subprocess

from .logging import Logger

def rclone_sync(remote: str, export_dir: str, logger: Logger):
    """DOC"""
    try:
        output = subprocess.check_output(f"rclone sync -P -v {export_dir} {remote}", shell=True, text=True)
        logger.write_log(output)
    except subprocess.CalledProcessError as exception_message:
        print(f"ERROR: {exception_message}")
        sys.exit(-1)
