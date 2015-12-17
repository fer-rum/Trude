__author__ = 'Fredo Erxleben'

import serial


class SerialDevice(object):
    """
    Describes a device which communicates through a serial interface
    """

    def __init__(self,
                 port,
                 host_encoding="utf-8",
                 host_eol="\r",
                 device_encoding="ascii",
                 device_eol="\n",
                 baud_rate=9600,
                 byte_size=serial.EIGHTBITS,
                 stop_bits=serial.STOPBITS_ONE,
                 parity=serial.PARITY_NONE,
                 timeout=10):
        """
        It is attempted to automatically connect via the given interface with the provided interfaces.
        :type port: str
        :type host_encoding:str A string representing the encoding used by the host machine.
        :type host_eol: str
        A string representing the end-of-line sequence to be appended by the host machine.
        It is automatically appended to any text given to send.
        :type device_encoding: str
        The encoding used by the device.
        :type device_eol: str
        :type baud_rate: int
        :type byte_size: int
        """

        self._host_encoding = host_encoding
        self._host_eol = host_eol
        self._device_encoding = device_encoding
        self._device_eol = device_eol  # TODO this is still ignored. How to get it working?
        self._connection = serial.Serial(port, baud_rate, byte_size, parity, stop_bits, timeout)

    @property
    def is_connected(self):
        if self._connection is None:
            return True
        else:
            return False

    def write_string(self, text: str):
        """
        Sends a string to the device.
        The specified host end of line sequence is appended automatically.
        Requires a connection to be established.
        :type text: str
        """

        assert self.is_connected
        text = "".join(text, self._host_eol)
        raw_bytes = text.encode(self._device_encoding)
        self._connection.write(raw_bytes)
        # TODO debug feedback about success

    def read_string(self):
        """
        Reads a line from the device and converts it into the encoding used by the host.
        :return: A string containing the host-encoded representation of the received data
        """
        assert self.is_connected
        raw_bytes = self._connection.readline()
        text = raw_bytes.decode(self._host_encoding)
        assert isinstance(text, str)
        return text