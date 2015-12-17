__author__ = 'Fredo Erxleben'

from drivers import SerialDeviceController as SDevController
from drivers import SerialDevice as SDev

from models import IselImc4Model

# TODO position should use proper units


class ISELMotorController(SDevController):
    """
    This class represents the control interface for a motor-driven 3-axis linear moving device produced by the company
    ISEL. The device is controlled by an IMC4 unit and connected via RS-232 to the host computer.

                    +------+         +---------+
                    |      |---------| Motor X |
                    |      | CAN-Bus +---------+
    +------+ RS-232 |      |         +---------+
    | Host |--------| IMC4 |---------| Motor Y |
    +------+        |      | CAN-Bus +---------+
                    |      |         +---------+
                    |      |---------| Motor Z |
                    +------+ CAN-Bus +---------+



    """

    def __init__(self, port, device_id: int=0):
        """

        :type port: str
        :param device_id: The identifying number of the device as used in the commands. This should be 0 unless multiple
        Isel-devices have been connected to the same control unit and you want to control the non-default device.
        """
        super(SDevController, self).__init__(SDev.SerialDevice(port))
        # TODO add support for configuration files

        self._deviceId = device_id
        self._initialized = False

        self._model = IselImc4Model()
        # TODO axis and position are now in the model

        self._position = None
        self._axisX = None
        self._axisY = None
        self._axisZ = None

    @property
    def is_initialized(self):
        return self._initialized

    def initialize(self):
        """

        :return: 'True' on successful initialization, 'False' otherwise
        """
        # TODO send init axis command
        self._initialized = False
        return False

    def force_initialization(self):
        self._initialized = True
        self._position = (0, 0, 0)

    def move_to(self, x, y, z):
        # TODO implement
        pass

    def move_by(self, x, y, z):
        # TODO implement
        pass

    @property
    def position(self):
        assert self.is_initialized
        return self._position

    @property
    def cover_open(self):
        assert self.is_initialized
        # TODO implement
        pass