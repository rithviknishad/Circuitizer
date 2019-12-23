import remi.gui as gui
from remi import start, App

import menuUI
import statusUI
import toolUI

class CircuitizerUI(App):
    def __init__(self, *args):
        super(CircuitizerUI, self).__init__(*args)

    def main(self):
        container = gui.Widget(width='100%', height='100%')
        
        container.style['background-color'] = '#1E1E1E'
        self.menu_layer = gui.Label(text="..")
        self.menu_layer.style['width'] = '100%'
        self.menu_layer.style['top'] = str(0)
        self.menu_layer.style['position'] = 'fixed'
        self.menu_layer.style['background-color'] = '#302d2d'
        container.append(self.menu_layer)

        for i in ['.']:
            container.append(menuUI.MenuUI(text=i))
        
        self.toolbar = gui.Label(text="..")
        self.toolbar.style['width'] = '100%'
        self.toolbar.style['top'] = str(15)
        self.toolbar.style['height'] = gui.to_pix(30)
        self.toolbar.style['position'] = 'fixed'
        self.toolbar.style['background-color'] = '#333333'

        container.append(self.toolbar)

        self.tool = toolUI.ToolUI(text="")
        # self.tool.add_class('fas fa-cloud')
        self.toolbar.append(self.tool)

        self.panel = gui.Widget()
        self.panel.style['position'] = 'fixed'
        self.panel.style['top'] = gui.to_pix(54)
        self.panel.style['width'] = gui.to_pix(250)
        self.panel.style['right'] = str(0)
        self.panel.style['color'] = 'white'
        self.panel.style['height'] = '90%'
        self.panel.style['background-color'] = '#252526'

        self.label = gui.Button(text="Inside?")
        self.label.style['color'] = 'white'
        self.panel.append(self.label)

        container.append(self.panel)

        self.actionbar = gui.Widget()
        self.actionbar.style['position'] = 'fixed'
        self.actionbar.style['top'] = gui.to_pix(54)
        self.actionbar.style['width'] = gui.to_pix(40)
        self.actionbar.style['left'] = str(0)
        self.actionbar.style['color'] = 'white'
        self.actionbar.style['height'] = '90%'
        self.actionbar.style['background-color'] = '#252526'

        container.append(self.actionbar)

        self.toolbar = gui.Widget()
        self.toolbar.style['position'] = 'fixed'
        self.toolbar.style['top'] = gui.to_pix(54)
        self.toolbar.style['width'] = gui.to_pix(250)
        self.toolbar.style['right'] = str(0)
        self.toolbar.style['color'] = 'white'
        self.toolbar.style['height'] = '90%'
        self.toolbar.style['background-color'] = '#252526'
        container.append(self.toolbar)

        container.append(statusUI.StatusUI(text=''))
        # returning the root widget
        return container


def do():
    start(CircuitizerUI, standalone=True, width=1000, height=600)

# starts the web server
if __name__ == "__main__":
    from multiprocessing import Process
    Process(target=do, args=()).start()
