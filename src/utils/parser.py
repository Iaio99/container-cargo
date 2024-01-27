"""DOC"""
import configparser
import sys

class ConfigManager:
    """DOC"""
    def __init__(self, config_file):
        config = configparser.ConfigParser()

        try:
            config.read(config_file)

            self._export_dir = config.get('General', 'EXPORT_DIR')
            self._log_filename = config.get('General', 'LOG_FILE')
            self._notify_via = config.get('General', 'NOTIFY_VIA')

            if self._notify_via == "telegram":
                self._telegram_options = dict()
                self._telegram_options["chat_id"] = config.get('Telegram', 'CHAT_ID')
                self._telegram_options["token"] = config.get('Telegram', 'TOKEN_API')

            elif self._notify_via == "mail":
                self._mail_options = dict()
                self._mail_options["sender"] = config.get('Mail', 'SENDER_ADDRESS')
                self._mail_options["password"] = config.get('Mail', 'PASSWORD')
                self._mail_options["smtp_server"] = config.get('Mail', 'SMTP_SERVER')

                if config.has_option('Mail', 'PORT'):
                    try:
                        self._mail_options["port"] = config.getint('Mail', 'PORT')
                    except ValueError:
                        print("ERROR: The port must be an integer")
                        sys.exit(-1)
                else:
                    self._mail_options["port"] = 465

                if config.has_option('Mail', 'RECEIVER_ADDRESS'):
                    self._mail_options["receiver"] = config.get('Mail', 'RECEIVER_ADDRESS')
                else:
                    self._mail_options["receiver"] = None

            else:
                print("ERROR: Method not implemented")
                sys.exit(-1)

        except (configparser.NoOptionError, configparser.NoSectionError) as exception_message:
            print(f"ERROR: {exception_message}")
            sys.exit(-1)

        try:
            self._docker_compose_dir = config.get('Containers', 'DOCKER_COMPOSE_DIR')
            self._lxc = config.getboolean('Containers', 'LXC')
        except configparser.NoOptionError:
            self._docker_compose_dir = None
            self._lxc = False
        except configparser.NoSectionError as exception_message:
            print(f"ERROR: {exception_message}")
            sys.exit(-1)

        try:
            self._rclone_remote = config.get('Drive', 'RCLONE_REMOTE')
        except (configparser.NoOptionError, configparser.NoSectionError):
            self._rclone_remote = None
        
        try:
            self._borg_user = config.get('Borg', 'BORG_USER')
            self._borg_host = config.get('Borg', 'BORG_HOST')
            self._borg_repo = config.get('Borg', 'BORG_REPO')
        except (configparser.NoOptionError, configparser.NoSectionError):
            self._borg_user = None
            self._borg_host = None
            self._borg_repo = None

    @property
    def lxc(self):
        """DOC"""
        return self._lxc

    @property
    def docker_compose_directory(self):
        """DOC"""
        return self._docker_compose_dir

    @property
    def log_filename(self):
        """DOC"""
        return self._log_filename

    @property
    def export_dir(self):
        """DOC"""
        return self._export_dir

    @property
    def rclone_remote(self):
        """DOC"""
        return self._rclone_remote

    @property
    def notify_via(self):
        """DOC"""
        return self._notify_via

    @property
    def notifier_options(self):
        """DOC"""
        if self._notify_via == "telegram":
            return self._telegram_options
        elif self._notify_via == "mail":
            return self._mail_options

    @property
    def borg_user(self):
        return self._borg_user
    
    @property
    def borg_host(self):
        return self._borg_host

    @property
    def borg_repo(self):
        return self._borg_repo
