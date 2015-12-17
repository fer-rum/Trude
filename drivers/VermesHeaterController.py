__author__ = 'Fredo Erxleben'

from drivers import SerialDeviceController as SDevController
from drivers import SerialDevice as SDev


class VermesHeaterController(SDevController):

    def __int__(self, port):
        super(SDevController, self).__init__(SDev.SerialDevice(port))