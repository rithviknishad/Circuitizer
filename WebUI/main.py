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
        self.menu_layer.style['background-color'] = '#333'
        container.append(self.menu_layer)

        for i in ['File', 'Edit', 'Tools']:
            container.append(menuUI.MenuUI(text=i))
        
        self.menu_layer = gui.Label(text="..")
        self.menu_layer.style['width'] = '100%'
        self.menu_layer.style['top'] = str(15)
        self.menu_layer.style['height'] = gui.to_pix(30)
        self.menu_layer.style['position'] = 'fixed'
        self.menu_layer.style['background-color'] = '#333'

        container.append(self.menu_layer)

        self.tool = toolUI.ToolUI(text="Hi")
        # self.tool.add_class('fas fa-cloud')
        self.menu_layer.append(self.tool)

        self.right_panel = gui.Widget()
        self.right_panel.style['position'] = 'fixed'
        self.right_panel.style['top'] = gui.to_pix(54)
        self.right_panel.style['width'] = gui.to_pix(250)
        self.right_panel.style['right'] = str(0)
        self.right_panel.style['color'] = 'white'
        self.right_panel.style['height'] = '90%'
        self.right_panel.style['background-color'] = '#252526'

        self.label = gui.Button(text="Inside?")
        self.label.style['color'] = 'white'
        self.right_panel.append(self.label)

        container.append(self.right_panel)

        self.toolbar = gui.Widget()
        self.toolbar.style['position'] = 'fixed'
        self.toolbar.style['top'] = gui.to_pix(54)
        self.toolbar.style['width'] = gui.to_pix(250)
        self.toolbar.style['right'] = str(0)
        self.toolbar.style['color'] = 'white'
        self.toolbar.style['height'] = '90%'
        self.toolbar.style['background-color'] = '#252526'
        container.append(self.toolbar)

        container.append(statusUI.StatusUI(text='Loading..'))
        # returning the root widget
        return container


def do():
    start(CircuitizerUI, standalone=True, width=1000, height=600)

# starts the web server
if __name__ == "__main__":
    from multiprocessing import Process
    Process(target=do, args=()).start()
