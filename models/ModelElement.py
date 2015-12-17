__author__ = 'Fredo Erxleben'


class ModelElement(object):

    # TODO add gui elements that represent each model element
    # TODO inherit properly from model element

    def __init__(self, sub_elements={}):

        self._sub_elements = sub_elements

    @property
    def sub_elements(self):
        return self._sub_elements