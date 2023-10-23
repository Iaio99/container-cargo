"""DOC"""
import os
import sys

from export import docker, lxc
from utils import logging, notification, parser, syncing

if __name__ == "__main__":
    if not os.path.exists("../config.ini"):
        print("ERROR: File ../config.ini not found")
        sys.exit(-1)
    else:
        config = parser.ConfigManager("../config.ini")

    export_dir = config.get_export_dir()

    logger = logging.Logger(config.get_log_filename())
    notifier_factory = notification.NotifierFactory()
    notifier = notifier_factory.create_notifier(config.get_notify_via(),
                                                **config.get_notifier_options())

    notifier.send_notification("Exporting containers...")

#    if config.get_lxc():
#        lxc_exporter = lxc.LxcExporter(export_dir)
#        lxc_exporter.export_containers(logger)
#        notifier.send_notification("LXC container exported with success!")

    if docker_compose_directory := config.get_docker_compose_directory():
        docker_compose_exporter = docker.DockerComposeExporter(export_dir, docker_compose_directory)
        docker_compose_exporter.export_containers(logger)
        notifier.send_notification("Docker compose exported with success!")

#    if rclone_remote := config.get_rclone_remote():
#        syncing.rclone_sync(rclone_remote, export_dir, logger)
#        notifier.send_notification("Sync complete!")

    notifier.send_notification("Export finished with no errors!")
    logger.close_log()
