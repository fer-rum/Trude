__author__ = 'fredo'


from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from models import ModelElement


class ModelElementWidget(GridLayout):

    def __init__(self, model_element: ModelElement):
        self.cols = 2
        for sub_element in model_element.items():
            self.add_widget(Label(str(sub_element[0])))
            # TODO decide the actual widget based on the type
            self.add_widget(Label(str(sub_element[1])))