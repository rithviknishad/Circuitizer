import os
import glob
import threading

import remi.gui as gui
from remi import start, App

import menuUI
import statusUI
import toolUI


def lazy_populate_project_files(self_pointer):
    pass


def lazy_load_css(self_pointer, url):
    self_pointer.execute_javascript("""
        var link = document.createElement('link')
        link.rel = 'stylesheet'
        link.href = \"""" + url + """\"
        document.getElementsByTagName('HEAD')[0].appendChild(link)
    """)


def lazy_load_js(self_pointer, url):
    self_pointer.execute_javascript("""
        var js = document.createElement('script')
        js.type = 'text/javascript'
        js.src = \"""" + url + """\"
        document.getElementsByTagName('HEAD')[0].appendChild(js)
    """)

items = {}

class w3_dropdown_hover(gui.Widget):
    def __init__(self, text=str(), stuffs=dict(), **kwargs):
        super(w3_dropdown_hover, self).__init__(text=str(), stuffs=dict(), **kwargs)
        global items
        items = stuffs
        self.style['background-color'] = '#302d2d'
        self.add_class('w3-dropdown-hover')

        class w3_dropdown_button(gui.Label):
            def __init__(self, **kwargs):
                super(w3_dropdown_button, self).__init__(**kwargs)

                self.add_class('bounceIn waves-effect waves-teal')
                self.set_style(menuUI.MenuCSS)

        self.append(w3_dropdown_button(text=text))

        class w3_dropdown_content(gui.Widget):
            def __init__(self, **kwargs):
                super(w3_dropdown_content, self).__init__(**kwargs)

                self.add_class('w3-dropdown-content w3-bar-block w3-card-4')
                self.style['color'] = '#969393'
                self.style['background-color'] = '#302d2d'

                class item(gui.Label):
                    def __init__(self, **kwargs):
                        super(item, self).__init__(**kwargs)
                        self.add_class('w3-bar-item w3-button')
                        self.onclick.do(lambda x: print(x))

                for key in items:
                    self.append(item(text=key))

        self.append(w3_dropdown_content())


class CircuitizerUI(App):
    def __init__(self, *args):
        super(CircuitizerUI, self).__init__(*args, static_file_path = {'my_resources': './res/'})
        for js in glob.glob('res/*.js'):
            lazy_load_js(self, "my_resources:" + os.path.basename(js))
        for css in glob.glob('res/*.css'):
            lazy_load_css(self, "my_resources:" + os.path.basename(css))
        lazy_load_css(self, "https://fonts.googleapis.com/icon?family=Material+Icons")
    
    def status_logic(self):
        self.status.set_text('Ready')

    def panel_logic(self):
        global lazy_populate_project_files
        self.properties_label = gui.Label(text="Properties Panel")
        self.properties_label.style['color'] = '#969393'
        self.properties_label.style['display'] = 'table-row'
        self.properties_label.style['padding'] = '10px 10px'
        self.panel.append(self.properties_label)

        self.properties_list_canvas = gui.Widget()
        self.properties_list_canvas.style['overflow-y'] = 'scroll'
        self.properties_list_canvas.style['overflow-x'] = 'scroll'
        self.properties_list_canvas.style['position'] = 'fixed'
        self.properties_list_canvas.style['width'] = '100%'
        self.properties_list_canvas.style['display'] = 'table-row'
        self.properties_list_canvas.style['height'] = '200px'
        self.properties_list_canvas.style['padding'] = '10px 10px'
        self.properties_list_canvas.style['background-color'] = '#252526'
        self.panel.append(self.properties_list_canvas)

        self.project_list_canvas = gui.Widget()
        self.project_list_canvas.style['display'] = 'table-row'
        self.project_list_canvas.style['overflow-y'] = 'scroll'
        self.project_list_canvas.style['overflow-x'] = 'scroll'
        self.project_list_canvas.style['position'] = 'fixed'
        self.project_list_canvas.style['height'] = '40%'
        self.project_list_canvas.style['width'] = '100%'
        self.project_list_canvas.style['bottom'] = '0'
        self.project_list_canvas.style['padding'] = '10px 10px'
        self.project_list_canvas.style['background-color'] = '#252526'
        self.panel.append(self.project_list_canvas)

        def lazy_populate_project_files(self_pointer):
            for file in glob.glob('*.*'):
                self_pointer.project_frame = gui.Widget()
                self_pointer.project_frame.style['background-color'] = '#252526'

                if os.path.isfile(file):
                    icon = gui.Label(text='description')
                else:
                    icon = gui.Label(text='folder')
                icon.style['color'] = '#969393'
                icon.add_class('material-icons')
                icon.style['display'] = 'table-cell'
                self_pointer.project_frame.append(icon)

                self_pointer.filename = gui.Label(text=file)
                self_pointer.filename.style['color'] = '#969393'
                self_pointer.filename.style['display'] = 'table-cell'
                self_pointer.filename.style['padding'] = '0px 20px'
                self_pointer.project_frame.append(self_pointer.filename)

                self_pointer.project_list_canvas.append(self_pointer.project_frame)

                icon.add_class('bounceIn')
                self_pointer.filename.add_class('bounceIn')


    def main(self):
        container = gui.Widget(width='100%', height='100%')       
        container.style['background-color'] = '#1E1E1E'

        self.menu_layer = gui.Label(text="..")
        self.menu_layer.style['width'] = '100%'
        self.menu_layer.style['top'] = str(0)
        self.menu_layer.style['position'] = 'fixed'
        self.menu_layer.style['background-color'] = '#302d2d'
        container.append(self.menu_layer)

        top = gui.Widget()
        top.style['display'] = 'table-cell'
        top.style['background-color'] = '#302d2d'
        top.add_class('w3-bar')

        for i in ['File', 'Edit', 'View', 'Go', 'Tools', 'Help']:
            top.append(w3_dropdown_hover(text=i, stuffs={'test': 0, 'test2': 0}))

        container.append(top)

        class toolbar(gui.Label):
            def __init__(self, **kwargs):
                super(toolbar, self).__init__(**kwargs)

                self.style['width'] = '100%'
                self.style['top'] = str(15)
                self.style['height'] = gui.to_pix(30)
                self.style['position'] = 'fixed'
                self.style['background-color'] = '#333333'

                class place_holder_text(toolUI.ToolUI):
                    def __init__(self, **kwargs):
                        super(place_holder_text, self).__init__(**kwargs)
                        pass
                
                self.append(place_holder_text(text='Toolbar'))
        
        container.append(toolbar(text='..'))

        self.panel = gui.Widget()
        self.panel.style['position'] = 'fixed'
        self.panel.style['top'] = gui.to_pix(54)
        self.panel.style['width'] = gui.to_pix(250)
        self.panel.style['right'] = str(0)
        self.panel.style['color'] = 'white'
        self.panel.style['height'] = '90%'
        self.panel.style['background-color'] = '#252526'

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
        self.canvas = gui.Label("Content")
        self.canvas.style['color'] = 'white'
        self.canvas.style['left'] = gui.to_pix(45)
        self.canvas.style['top'] = gui.to_pix(55)
        self.canvas.style['right'] = gui.to_pix(250)
        self.canvas.style['bottom'] = gui.to_pix(28)
        self.canvas.style['position'] = 'fixed'
        self.canvas.style['background-color'] = '#1E1E1E'
        container.append(self.canvas)

        self.status = statusUI.StatusUI(text='Loading...')
        container.append(self.status)

        threading.Thread(target=self.panel_logic, args=()).start()
        threading.Thread(target=self.status_logic(), args=()).start()
        threading.Thread(target=lazy_populate_project_files, args=(self, )).start()

        # returning the root widget
        return container

def do():
    start(CircuitizerUI, standalone=True, width=1000, height=600)
    # start(CircuitizerUI)

# remi==2019.9 nuitka
# starts the web server
if __name__ == "__main__":
    do()
