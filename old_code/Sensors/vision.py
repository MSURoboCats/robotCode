from static_utilities import StaticUtilities


class Vision:

    def __init__(self, name: str = "Vision Object") -> None:
        self.name: str = name
        StaticUtilities.logger.info(f"{self.name} initialized")
