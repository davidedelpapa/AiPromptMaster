"""
Logger functions
"""
import logging
from os import PathLike, getenv
from typing import Union


# TODO: migrating to Pyhton 3.10+, the following should be
#       def configure_logging(loggername: str, filename: str | PathLike) -> logging.Logger:
#       removing the Union import
def configure_logging(
    loggername: str, filename: Union[str, PathLike]
) -> logging.Logger:
    """
    Logging configuration, with sensible defaults for the whole project

    :param loggername: name to set for the logger
    :param filename: path where to save the log to
    :return: a constructed Logger
    """
    build = getenv("BUILD", "RELEASE")

    logging.basicConfig(
        filename=filename,
        filemode="a",
        format="%(asctime)s.%(msecs)d-%(name)s-%(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger(loggername)

    if build == "RELEASE":
        logger.setLevel("ERROR")
    else:
        logger.setLevel("DEBUG")

    return logger
