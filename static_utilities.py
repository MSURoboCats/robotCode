import logging
import os
import pathlib
from logging import Logger
from typing import Tuple, List

from custom_formatter import CustomFormatter


class StaticUtilities:
    _project_root_directory_str: pathlib.Path = pathlib.Path(str(pathlib.Path(__file__).parent))

    # create logger
    logger: Logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    # setup file logger and add to logger
    try:
        log_path: pathlib.Path = _project_root_directory_str / 'log.log'
        if os.path.exists(log_path):
            os.remove(log_path)
        file_logging_handler = logging.FileHandler(log_path)
        file_logging_handler.setFormatter(
            logging.Formatter('%(levelname)s %(module)s %(funcName)s %(message)s'))
        file_logging_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_logging_handler)
    except PermissionError:
        pass

    # setup extended file logger and add to logger
    extended_log_path: pathlib.Path = _project_root_directory_str / 'extended_log.log'
    extended_file_logging_handler = logging.FileHandler(extended_log_path)
    extended_file_logging_handler.setFormatter(
        logging.Formatter('%(levelname)s %(module)s %(funcName)s %(message)s'))
    extended_file_logging_handler.setLevel(logging.DEBUG)
    logger.addHandler(extended_file_logging_handler)

    @staticmethod
    def serial_devices() -> List[Tuple[str, str, str]]:
        """
        :returns: List of serial devices as a Tuple with the format (port,description,HardwareID). See class serial.tools.list_ports.ListPortInfo
        """
        import serial.tools.list_ports
        return [tuple(p) for p in list(serial.tools.list_ports.comports())]
