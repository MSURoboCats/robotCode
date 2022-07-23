from multiprocessing import Queue

from process_queue_data import ProcessQueueData
from static_utilities import StaticUtilities
from subsystem import Subsystem


class Vision(Subsystem):

    def __init__(self, name: str = "Vision Object") -> None:
        super().__init__(name, "", 0)
        StaticUtilities.logger.info(f"{self.name} initialized")

    def run(self, send_queue: "Queue[ProcessQueueData]", receive_queue: "Queue[ProcessQueueData]") -> None:
        while self.running:
            pass
