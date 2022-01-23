from static_utilities import StaticUtilities


class Torpedo:

    def __init__(self, *, name: str = "torpedo") -> None:
        self.name: str = name
        StaticUtilities.logger.info(f"{self.name} initialized")
        