from copy import deepcopy
from enum import Enum
from typing import List, Any


class ProcessQueueDataType(Enum):
    """
    Encoded representation of the data type expected from the sender for given data.
    """
    MAIN: 0  # str
    ARDUINO_INTERFACE: 1  # None?
    VISION: 2  # ???
    IMU: 3  # List[?]


class ProcessQueueDataPriority(Enum):
    """
    Encoded representation of the priority of the data from the sender including hints on how the data should be handled or processed.
    """
    URGENT: 0  # triggers lock on MAIN
    UPDATE: 1  # update from a sensor or subsystem
    NAVIGATION_UPDATE: 2  # data that should cause course correction or manipulation probably requiring additional computation


class ProcessQueueData:
    """
    TODO: replace the whole queue with a priority queue.
    """

    def __init__(self, data_type: ProcessQueueDataType, priority: ProcessQueueDataPriority, data: Any) -> None:
        self._data_type: ProcessQueueDataType = deepcopy(data_type)
        self._priority: ProcessQueueDataPriority = deepcopy(priority)
        self._data: Any = deepcopy(data)

    def priority(self) -> ProcessQueueDataPriority:
        return self._priority

    def data_type(self) -> ProcessQueueDataType:
        return self._data_type.value

    def data(self) -> Any:
        return self._data
