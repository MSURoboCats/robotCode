from Sensors.sensor import Sensor
from static_utilities import StaticUtilities


class DepthPressure(Sensor):

    def __init__(self, *, name: str = "Depth and Pressure Sensor") -> None:
        super().__init__(name=name)
        print(self.name)
