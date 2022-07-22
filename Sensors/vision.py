from multiprocessing import Queue

from process_queue_data import ProcessQueueData
from static_utilities import StaticUtilities


class Vision:

    def __init__(self, name: str = "Vision Object") -> None:
        self.name: str = name
        self.running: bool = True
        StaticUtilities.logger.info(f"{self.name} initialized")

    def run(self, process_queue: Queue[ProcessQueueData]) -> None:
        while self.running:
            pass
