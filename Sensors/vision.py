from static_utilities import StaticUtilities


class Vision:

    def __init__(self, name: str = "Vision Object") -> None:
        self.name: str = name
        self.running: bool = True
        StaticUtilities.logger.info(f"{self.name} initialized")

    def run(self) -> None:
        while self.running:
            pass
