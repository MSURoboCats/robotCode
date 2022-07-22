from copy import deepcopy
from enum import Enum
from typing import List, Any


class ProcessQueueDataType(Enum):
    MAIN: 0
    ARDUINO_INTERFACE: 1
    VISION: 2
    IMU: 3


class ProcessQueueData:

    def __init__(self, data_type: ProcessQueueDataType, priority: int, data: List[Any]) -> None:
        self._data_type: ProcessQueueDataType = deepcopy(data_type)
        self._priority: int = deepcopy(priority)
        self._data: List[Any] = deepcopy(data)

    def priority(self) -> int:
        return self._priority

    def data_type(self) -> ProcessQueueDataType:
        return self._data_type.value

    def data(self) -> List[Any]:
        return self._data
