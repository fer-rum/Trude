__author__ = 'Fredo Erxleben'


class DeviceModel(object):
    """
    A device model is the combination of properties and states associated with a device.
    Any state or property changing functionality a device exposes, should be reflected in the model as well.
    """

    def __init__(self, device_type="Unknown device"):
        self._deviceType = device_type
        self._components = {}

    @property
    def list_components(self):
        return self._components.keys()

    def add_component(self, name, instance):
        self._components[name] = instance