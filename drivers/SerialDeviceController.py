__author__ = 'Fredo Erxleben'

from drivers import Command
from drivers import SerialDevice
from drivers import CommunicationMode


class SerialDeviceController(object):

    def __init__(self, device: SerialDevice, mode: CommunicationMode=CommunicationMode.HALF_DUPLEX):
        assert device is SerialDevice
        assert device.is_connected
        self._device = device
        self._communication_mode = mode

        if not mode.rw_exclusive:
            raise NotImplementedError("Only rw exclusive communication is currently supported.")

    @property
    def device(self):
        return self._device

    def issue_command(self, command: Command):
        """
        Issues a given command to the device.
        If the command expects a reply, it is read and given to the commands reply handling method.
        :param command: The object that represents the command that has to be issued.
        :return:
        """
        self._device.write_string(str(command))
        if command.expects_reply:
            reply = self._device.read_string()
            command.handle_reply(reply)