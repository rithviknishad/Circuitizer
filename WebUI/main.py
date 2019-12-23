import remi.gui as gui
from remi import start, App

import menuUI
import statusUI


class CircuitizerUI(App):
    def __init__(self, *args):
        super(CircuitizerUI, self).__init__(*args)

    def main(self):
        container = gui.Widget(width='100%', height='100%')
        container.style['background-color'] = '#1E1E1E'
        

        self.menu_layer = gui.Label(text="Loading..")
        self.menu_layer.style['width'] = '100%'
        self.menu_layer.style['top'] = str(0)
        self.menu_layer.style['position'] = 'fixed'
        self.menu_layer.style['background-color'] = '#333'
        container.append(self.menu_layer)

        container.append(menuUI.MenuUI(text='File'))
        container.append(menuUI.MenuUI(text='Edit'))
        container.append(menuUI.MenuUI(text='Tools'))

        container.append(statusUI.StatusUI(text=' Ready'))
        # returning the root widget
        return container

# starts the web server
if __name__ == "__main__":
    start(CircuitizerUI, standalone=True)
