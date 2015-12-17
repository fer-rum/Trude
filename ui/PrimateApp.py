__author__ = 'Fredo Erxleben'

# PriMaTE = Printer Management Tool Engine

from kivy.app import App
from kivy.app import Builder


class PrimateApp(App):

    def build(self):
        self.root = Builder.load_file('Primate.kv')

if __name__ == '__main__':
    PrimateApp().run()
