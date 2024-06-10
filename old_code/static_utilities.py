import logging
from logging import Logger


class StaticUtilities:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt="%m-%d-%Y %H:%M:%S")
    logger: Logger = logging.getLogger(__name__)
