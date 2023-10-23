"""DOC"""

class Logger:
    """DOC"""
    def __init__(self, filename: str):
        self._log_file = open(filename, "a", encoding="UTF-8")

    def write_log(self, msg: str):
        """DOC"""
        self._log_file.write(msg+"\n")

    def close_log(self):
        """DOC"""
        self._log_file.close()
        del self
