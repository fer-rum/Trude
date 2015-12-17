__author__ = 'Fredo Erxleben'

from enum import Enum


class CommunicationMode(Enum):
    READ_SIMPLEX = (True, False, False)
    WRITE_SIMPLEX = (False, True, False)
    HALF_DUPLEX = (True, True, True)
    FULL_DUPLEX = (True, True, False)

    def __init__(self, read: bool, write: bool, exclusive: bool):
        self._write_allowed = write
        self._read_allowed = read
        self._rw_exclusive = exclusive

    @property
    def write_allowed(self):
        return self._write_allowed

    @property
    def read_allowed(self):
        return self._read_allowed

    @property
    def rw_exclusive(self):
        return self._rw_exclusive
