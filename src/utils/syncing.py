"""DOC"""
import os
import sys
import subprocess
import time

from .logging import Logger

def rclone_sync(remote: str, export_dir: str, logger: Logger):
    """DOC"""
    try:
        output = subprocess.check_output(f"rclone sync -P -v {export_dir} {remote}", shell=True, text=True)
        logger.write_log(output)
    except subprocess.CalledProcessError as exception_message:
        print(f"ERROR: {exception_message}")
        sys.exit(-1)

def borg_sync(user:str, host: str, repos_folder: str, path_ssh_key: str, export_dir: str, logger: Logger):
    """DOC"""
    if path_ssh_key:
        os.environ["BORG_RSH"] = f"ssh -i {path_ssh_key}"
    output = os.system(f"""borg create --stats ssh://{user}@{host}{repos_folder}/Containers::Containers-{time.strftime('%Y-%m-%d-%H%M%S', time.gmtime())} {export_dir}""")