import logging


class LogLevelFilter(logging.Filter):
    __levels = None

    def __init__(self, levels=None):
        super().__init__()
        self.__levels = levels

    def filter(self, record: logging.LogRecord) -> int:
        return record.levelname in self.__levels
