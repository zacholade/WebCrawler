import logging


ROOT_LOGGER_NAME = "webcrawler"


class LoggingMixin:

    @property
    def logger(self) -> logging.Logger:
        name = '.'.join([ROOT_LOGGER_NAME, self.__module__, self.__class__.__name__])
        return logging.getLogger(name)
