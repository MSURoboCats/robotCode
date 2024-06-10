from static_utilities import StaticUtilities


class Sensor:
    """
    A sensor from which all other sensors must inherit.
    """

    def __init__(self, name: str, *, init_message: str = None) -> None:
        self.name: str = name
        StaticUtilities.logger.info(f"Sensor: {self.name} initialized" if init_message is None else init_message)
