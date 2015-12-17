__author__ = 'Fredo Erxleben'

from models import ModelElement
from enum import Enum


class Endstop(ModelElement):
    """
    Abstracts an endstop on a linear axis.
    """

    def __init__(self):
        self._triggered = False

    @property
    def triggered(self):
        return self._triggered

    def trigger(self):
        self._triggered = True

    def release(self):
        self._triggered = False


class EndstopPosition(Enum):
    MIN = 0
    MAX = 1


class Axis(ModelElement):
    # TODO implement axis size in proper units
    # TODO check if both endstops are triggered at the same time...

    def __init__(self, has_min_endstop: bool=True, has_max_endstop: bool=True):

        self._endstops[EndstopPosition.MIN] = Endstop() if has_min_endstop else None
        self._endstops[EndstopPosition.MAX] = Endstop() if has_max_endstop else None

    @property
    def has_min_endstop(self):
        if self._endstops[EndstopPosition.MIN] is None:
            return False
        else:
            return True

    @property
    def has_max_endstop(self):
        if self._endstops[EndstopPosition.MAX] is None:
            return False
        else:
            return True

    @property
    def endstop_min(self):
        return self._endstops[EndstopPosition.MIN]

    @property
    def endstop_max(self):
        return self._endstops[EndstopPosition.MAX]

    def trigger(self, endstop_position: EndstopPosition):
        if self._endstops[endstop_position] is None:
            return
        self._endstops[endstop_position].trigger()

    def release(self, endstop_position: EndstopPosition):
        if self._endstops[endstop_position] is None:
            return
        self._endstops[endstop_position].release()