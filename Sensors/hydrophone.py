from static_utilities import StaticUtilities


class Hydrophone:

    def __init__(self, name: str = "Hydrophone Object") -> None:
        self.name: str = name
        StaticUtilities.logger.info(f"{self.name} initialized")
