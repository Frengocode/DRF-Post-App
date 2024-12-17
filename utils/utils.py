import logging
import colorlog

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

handler = colorlog.StreamHandler()

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    log_colors={
        "DEBUG": "blue",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

handler.setFormatter(formatter)

log.addHandler(handler)
