"""DOC"""
import os
import sys

from export import docker, lxd, incus
from utils import logging, notification, parser, syncing, remove_exported_containers

if __name__ == "__main__":
    if not os.path.exists("/etc/container-cargo/config.ini"):
        print("ERROR: File /etc/container-cargo/config.ini not found")
        sys.exit(-1)
    else:
        config = parser.ConfigManager("/etc/container-cargo/config.ini")

    export_dir = config.export_dir

    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    logger = logging.Logger(config.log_filename)
    notifier_factory = notification.NotifierFactory()
    notifier = notifier_factory.create_notifier(config.notify_via,
                                                **config.notifier_options)

    notifier.send_notification("Exporting containers...")

    if config.lxd:
        lxd_exporter = lxd.LxdExporter(export_dir)
        lxd_exporter.export_containers(logger)
        notifier.send_notification("LXD container exported with success!")

    if config.incus:
        incus_exporter = incus.IncusExporter(export_dir)
        incus_exporter.export_containers(logger)
        notifier.send_notification("Incus container exported with success!")

    if docker_compose_directory := config.docker_compose_directory:
        docker_compose_exporter = docker.DockerComposeExporter(export_dir, docker_compose_directory)
        docker_compose_exporter.export_containers(logger)
        notifier.send_notification("Docker compose exported with success!")

    if rclone_remote := config.rclone_remote:
        syncing.rclone_sync(rclone_remote, export_dir, logger)
        notifier.send_notification("Sync complete!")

    else:
        borg_user = config.borg_user
        borg_host = config.borg_host
        borg_repo = config.borg_repo
        path_ssh_key = config.path_ssh_key

        if borg_user and borg_host and borg_repo:
            syncing.borg_sync(borg_user, borg_host, borg_repo, path_ssh_key, export_dir, logger)
            notifier.send_notification("Sync complete!")

    notifier.send_notification("Export finished with no errors!")
    logger.close_log()
    remove_exported_containers(export_dir)