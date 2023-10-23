"""Doc"""

import sys
import smtplib
import ssl

from abc import ABC, abstractmethod

import requests


class Notifier(ABC):
    "DOC"
    def __init__(self):
        pass

    @abstractmethod
    def send_notification(self, msg):
        """DOC"""


class NotifierFactory:
    "DOC"
    def create_notifier(self, extern, **kwargs):
        "DOC"
        if extern == "telegram":
            chat_id = kwargs.get("chat_id")
            token = kwargs.get("token")

            return TelegramNotifier(chat_id, token)

        elif extern == "email":
            sender = kwargs.get("sender")
            password = kwargs.get("password")
            smtp_server = kwargs.get("smtp_server")
            port = kwargs.get("port", 465)
            receiver = kwargs.get("receiver", None)

            return EmailNotifier(sender, password, smtp_server, port, receiver)


class TelegramNotifier(Notifier):
    "DOC"
    def __init__(self, chat_id, token):
        self._token = token
        self._chat_id = chat_id

    def send_notification(self, msg):
        """This function send a notification via Telegram using HTTP API"""

        tlg_msg = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chat_id}&text={msg}"

        return requests.get(tlg_msg, timeout=50)


class EmailNotifier(Notifier):
    "DOC"
    def __init__(self, sender, password, smtp_server, port=465, receiver=None):
        self._sender = sender
        self._password = password
        self._smtp_server = smtp_server
        self._port = port

        if receiver is None:
            self._receiver = self._sender
        else:
            self._receiver = receiver

    def send_notification(self, msg):
        "DOC"
        context = ssl.create_default_context()

        if self._port == 465:
            with smtplib.SMTP_SSL(self._smtp_server, self._port, context=context) as server:
                server.login(self._sender, self._password)
                return server.sendmail(self._sender, self._receiver, msg)
        elif self._port == 587:
            with smtplib.SMTP(self._smtp_server, self._port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(self._sender, self._password)
                return server.sendmail(self._sender, self._receiver, msg)
        else:
            print("ERROR: Use standard ports (465 or 587)")
            sys.exit(-1)
