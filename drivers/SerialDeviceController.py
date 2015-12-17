__author__ = 'Fredo Erxleben'


from drivers import SerialDevice
from drivers import CommunicationMode

from threading import Thread
from threading import Lock
from threading import Event

# TODO enable the abstraction of commands and the issuing of such


class SerialDeviceController(object):

    def __init__(self, device: SerialDevice, mode: CommunicationMode=CommunicationMode.HALF_DUPLEX):
        assert device is SerialDevice
        assert device.is_connected
        self._device = device
        self._communication_mode = mode
        self._read_thread = Thread(name="Reader", target=self._read())
        self._write_thread = Thread(name="Writer", target=self._write())
        self._terminate_reader = Event()
        self._terminate_writer = Event()

        # If the communication mode forbids contemporary reading and writing,
        # a lock will be needed
        if mode.rw_exclusive:
            self._io_lock = Lock()

    @property
    def device(self):
        return self._device

    # TODO implement proper error handling

    def _start_reader(self):
        if not self._read_thread.is_alive():
            self._read_thread.start()

    def _stop_reader(self):
        if self._read_thread.is_alive():
            self._terminate_reader.set()
            self._read_thread.join()
            self._terminate_reader.clear()

    def _start_writer(self):
        if not self._write_thread.is_alive():
            self._write_thread.start()

    def _stop_writer(self):
        if self._write_thread.is_alive():
            self._terminate_writer.set()
            self._write_thread.join()
            self._terminate_writer.clear()

    def _read(self):
        """
        Attempts repeatedly to read a line from the device and hand it over to the parsing function.
        If the communication mode is read-write exclusive, a lock will be acquired beforehand
        and be released immediately after reading.
        The read line then will be passed into the parse_read_line function for further handling.
        :return:
        """

        while not self._terminate_reader.is_set():

            if self._communication_mode.rw_exclusive:
                self._io_lock.acquire()  # caution: blocking!

            line = self._device.read_string()

            if self._communication_mode.rw_exclusive:
                self._io_lock.release()

            self.parse_read_line(line)

    def _write(self):
        # TODO implement
        pass

    def parse_read_line(self, incoming: str):
        """
        This method is supposed to be overridden by inheriting children.
        :param incoming:
        :return:
        """
        pass



