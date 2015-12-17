__author__ = 'Fredo Erxleben'

from models import DeviceModel
from models import Axis


class IselImc4Model(DeviceModel):

    AXIS_X = 'Axis X'
    AXIS_Y = 'Axis Y'
    AXIS_Z = 'Axis Z'
    COVER = 'Cover'
    KEY = 'Key'
    # TODO what else does this control?

    def __init__(self):
        super(DeviceModel).__init__("Isel IMC4 Device")

        self._position = (0, 0, 0)

        self.add_component(IselImc4Model.AXIS_X, Axis(True, True))
        self.add_component(IselImc4Model.AXIS_X, Axis(True, True))
        self.add_component(IselImc4Model.AXIS_X, Axis(True, True))
        # TODO continue

