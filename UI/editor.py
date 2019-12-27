#!/usr/bin/python3
# Circuitizer UI

import sys
sys.dont_write_bytecode = True

import os
import glob
import json
import time
import webview
import threading

import remi.gui as gui
from remi import start, App

import UI.menuUI as menuUI
import UI.statusUI as statusUI
import UI.toolUI as toolUI

from UI.extras import *

# Load the configuration file for Circuitizer
config = json.load(open('UI/config.json'))
# Locate the resource folder
RES_PATH = './UI/res/'


class w3_dropdown_hover(gui.Widget):
    def __init__(self, text=str(), stuffs=dict(), **kwargs):
        super(w3_dropdown_hover, self).__init__(text=str(), stuffs=dict(), **kwargs)
        global items
        items = stuffs
        self.style['background-color'] = config["primary-background-color"]
        self.add_class('w3-dropdown-hover')

        class w3_dropdown_button(gui.Label):
            def __init__(self, **kwargs):
                super(w3_dropdown_button, self).__init__(**kwargs)

                self.add_class('bounceIn')
                self.set_style(menuUI.MenuCSS)

        self.append(w3_dropdown_button(text=text))

        class w3_dropdown_content(gui.Widget):
            def __init__(self, **kwargs):
                super(w3_dropdown_content, self).__init__(**kwargs)

                self.style['color'] = config["primary-foreground-color"]
                self.style['background-color'] = config["primary-background-color"]
                self.add_class('w3-dropdown-content w3-bar-block w3-card-4')

                class item(gui.Label):
                    def __init__(self, **kwargs):
                        super(item, self).__init__(**kwargs)

                        self.style['font-size'] = config['font-size-dropbox-item']
                        self.add_class('w3-bar-item w3-button w3-animate-top')
                        self.onclick.do(event)

                for key in items:
                    global event
                    event = items[key]
                    self.append(item(text=key))

        self.append(w3_dropdown_content())


class CircuitizerUI(App):
    def __init__(self, *args):
        super(CircuitizerUI, self).__init__(*args, static_file_path = {'my_resources': RES_PATH})
        lazy_load_http_equiv(self)
        inject_css_scrollbar(self)
        lazy_load_css(self, "https://fonts.googleapis.com/icon?family=Material+Icons")
        if config["cdn-or-local"] == 'cdn':
            lazy_load_css(self, "https://www.w3schools.com/w3css/4/w3.css")
            lazy_load_css(self, "https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css")
            lazy_load_css(self, "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css")
            lazy_load_js(self, "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js")
        else:
            for js in glob.glob(RES_PATH + '*.js'):
                lazy_load_js(self, "my_resources:" + os.path.basename(js))
            for css in glob.glob(RES_PATH + '*.css'):
                lazy_load_css(self, "my_resources:" + os.path.basename(css))
        start_status_thread = threading.Thread(target=self.status_logic, args=())
        start_status_thread.daemon = True
        start_status_thread.start()

    def new_project_tab(self, event):
        self.canvas.empty()
        f1 = gui.Widget()
        f1.add_class('w3-container z-depth-5')
        f1.style['width'] = '100%'
        f1.style['padding'] = '10px 10px'
        f1.style['background-color'] = config["primary-background-color"]
        
        foo = gui.Label('Project Name ')
        foo.style['color'] = config["primary-foreground-color"]
        foo.style['font-size'] = 'x-large'
        foo.style['padding'] = '10px 10px 10px 10px'

        project_name = gui.TextInput(hint='Enter your project name here')
        project_name.style['background-color'] = config["primary-background-color"]
        project_name.style['height'] = gui.to_pix(43)
        project_name.add_class('input-field waves-light')
        project_name.style['padding'] = gui.to_pix(10)

        ok_button = gui.Label(text='Create')
        ok_button.add_class('w3-button')
        ok_button.style['padding'] = gui.to_pix(10)

        def project_startup_page():
            self.canvas.empty()
            foo = gui.Label(project_name.get_text() + '.cxproj Project')
            foo.add_class('w3-jumbo')
            foo.style['height'] = '60px'
            foo.style['padding'] = '10px 10px 10px 10px'

            create_schematic_button = gui.Label('Schematic')
            foo = gui.Widget()
            foo.add_class('material-icons')
            foo.type = 'i'
            create_schematic_button.append(foo)
            create_schematic_button.add_class('w3-button')

            create_component_button = gui.Label('Custom component definition')
            create_component_button.add_class('w3-button')

            create_cppscript_button = gui.Label('C++ Script')
            create_cppscript_button.add_class('w3-button')

            link_compiler_button = gui.Label('Link custom compiler suite')
            link_compiler_button.add_class('w3-button')

            for widget in [
                    foo, create_schematic_button,
                    create_component_button, create_cppscript_button,
                    link_compiler_button
                ]:
                self.canvas.append(widget)

        
        def project_event(e):
            
            project_format_file_handler = open(project_name.get_text() + '.cxproj', 'w')
            project_format_file_handler.write('')
            project_format_file_handler.close()
            project_startup_page()

        ok_button.onclick.do(project_event)

        for widget in [foo, project_name, ok_button]:
            f1.append(widget)
        
        for widget in [f1]:
            self.canvas.append(widget)

    def status_logic(self):
        time.sleep(3)
        self.status.set_text('Ready')

    def panel_logic(self):
        global lazy_populate_project_files
        self.properties_label = gui.Label(text="Properties Panel")
        self.properties_label.style['color'] = config["primary-foreground-color"]
        self.properties_label.style['display'] = 'table-row'
        self.properties_label.style['position'] = 'relative'
        self.panel.append(self.properties_label)

        self.properties_list_canvas = gui.Widget()
        self.properties_list_canvas.style['overflow-y'] = 'scroll'
        self.properties_list_canvas.style['overflow-x'] = 'scroll'
        self.properties_list_canvas.style['position'] = 'relative'
        self.properties_list_canvas.style['width'] = '100%'
        self.properties_list_canvas.style['display'] = 'table-row'
        self.properties_list_canvas.style['height'] = '250px'
        self.properties_list_canvas.style['background-color'] = config["panel-background-color"]
        self.panel.append(self.properties_list_canvas)

        self.properties_label = gui.Label(text="Project Panel")
        self.properties_label.style['color'] = config["primary-foreground-color"]
        self.properties_label.style['display'] = 'table-row'
        self.properties_label.style['position'] = 'relative'
        self.panel.append(self.properties_label)

        self.project_list_canvas = gui.Widget()
        self.project_list_canvas.style['display'] = 'table-row'
        self.project_list_canvas.style['overflow-y'] = 'scroll'
        self.project_list_canvas.style['overflow-x'] = 'scroll'
        self.project_list_canvas.style['position'] = 'fixed'
        self.project_list_canvas.style['height'] = '40%'
        self.project_list_canvas.style['width'] = str(gui.to_pix(int(config["panel-width"]) - 10))
        self.project_list_canvas.style['bottom'] = '22px'
        self.project_list_canvas.style['background-color'] = config["panel-background-color"]
        self.panel.append(self.project_list_canvas)

        def lazy_populate_project_files(self_pointer):
            for file in glob.glob('*'):
                self_pointer.project_frame = gui.Widget()
                self_pointer.project_frame.style['background-color'] = config["panel-background-color"]

                if os.path.isfile(file):
                    icon = gui.Label(text='description')
                else:
                    icon = gui.Label(text='folder')
                icon.style['color'] = config["primary-foreground-color"]
                icon.add_class('material-icons')
                icon.style['display'] = 'table-cell'
                self_pointer.project_frame.append(icon)

                self_pointer.filename = gui.Label(text=file)
                self_pointer.filename.style['color'] = config["primary-foreground-color"]
                self_pointer.filename.style['display'] = 'table-cell'
                self_pointer.filename.style['padding'] = '0px 20px'
                self_pointer.project_frame.append(self_pointer.filename)

                self_pointer.project_list_canvas.append(self_pointer.project_frame)

                icon.add_class('bounceIn')
                self_pointer.filename.add_class('bounceIn')


    def main(self):
        container = gui.Widget(width='100%', height='100%')       
        container.style['background-color'] = config["canvas-background-color"]

        self.menu_layer = gui.Label(text="..")
        self.menu_layer.style['width'] = '100%'
        self.menu_layer.style['top'] = str(0)
        self.menu_layer.style['position'] = 'fixed'
        self.menu_layer.style['background-color'] = config["menu-background-color"]
        container.append(self.menu_layer)

        top = gui.Widget()
        top.style['display'] = 'table-cell'
        top.style['background-color'] = config["menu-background-color"]
        top.add_class('w3-bar')

        MENUS = {
            'File': {
                'New Project': self.new_project_tab,
                'New Schematic': print,
                'New Component Definition': print,
                'New Simulation Card': print,
                'New Python Script': print,
                'New C++ Class': print,
                '': print,
                'Open Project': print,
                'Open File': print,

                'Save': print,
                'Save As': print,
                'Save All': print,

                'Install Extensions': print,

                'Update Extensions': print,
                'Update Circuitizer': print,

                'Close Window': print,
                'Restart UI Service': print,
            },
            'Edit': {
                'Undo': print,
                'Redo': print,
                '': print,
                'Cut': print,
                'Copy': print,
                'Paste': print,
                '.': print,
                'Find': print,
                'Replace': print,
            },
            'View': {
                'Command Panel': print,
                'Appearance': print,
                '': print,
                'Output': print,
                'Log Fish': print,
                'Editor Layout': print,
                'File Explorer': print,
                'Extension Manager': print,
                '.': print,
                'Toggle Side Panel': print,
                'Toggle Tool Bar': print,
                'Toggle Action Bar': print,
                'Toggle Status Bar': print,
            },
            'Help': {
                'Welcome Notes': print,
                'Tutorials': print,
                '': print,
                'Documentation': print,
                'Keyboard Shortcuts': print,
                'What\'s new': print,
                'Donate': print,
                'About': print,
            },

        }
        for menu in MENUS:
            top.append(w3_dropdown_hover(text=menu, stuffs=MENUS[menu]))

        container.append(top)

        class toolbar(gui.Label):
            def __init__(self, **kwargs):
                super(toolbar, self).__init__(**kwargs)

                self.style['width'] = '100%'
                self.style['top'] = str(15)
                self.style['height'] = gui.to_pix(30)
                self.style['position'] = 'fixed'
                self.style['background-color'] = config["tool-background-color"]

                class place_holder_text(toolUI.ToolUI):
                    def __init__(self, **kwargs):
                        super(place_holder_text, self).__init__(**kwargs)
                        pass
                
                self.append(place_holder_text(text='Toolbar'))
        
        container.append(toolbar(text='..'))

        self.panel = gui.Widget()
        self.panel.style['position'] = 'absolute'
        self.panel.style['top'] = gui.to_pix(54)
        self.panel.style['width'] = gui.to_pix(int(config["panel-width"]))
        self.panel.style['right'] = str(0)
        self.panel.style['color'] = 'white'
        self.panel.style['height'] = '90%'
        self.panel.style['background-color'] = config["panel-background-color"]
        self.panel.style['padding'] = '10px 10px'

        container.append(self.panel)

        self.actionbar = gui.VBox()
        self.actionbar.style['position'] = 'fixed'
        self.actionbar.style['top'] = gui.to_pix(54)
        self.actionbar.style['width'] = gui.to_pix(40)
        self.actionbar.style['left'] = str(0)
        self.actionbar.style['color'] = config["primary-foreground-color"]
        self.actionbar.style['height'] = '90%'
        self.actionbar.style['background-color'] = config["panel-background-color"]

        container.append(self.actionbar)

        self.canvas = gui.Widget()
        self.canvas.style['position'] = 'fixed'
        self.canvas.style['top'] = gui.to_pix(55)
        self.canvas.style['left'] = gui.to_pix(45)
        self.canvas.style['bottom'] = gui.to_pix(28)
        self.canvas.style['right'] = gui.to_pix(int(config["panel-width"]))
        self.canvas.style['color'] = config["primary-foreground-color"]
        self.canvas.style['background-color'] = config["canvas-background-color"]
        self.canvas.style['padding'] = ' '.join([gui.to_pix(10), gui.to_pix(10)])
        container.append(self.canvas)

        self.status = statusUI.StatusUI(text='Please wait while background service is loading...')
        container.append(self.status)

        threading.Thread(target=self.panel_logic, args=()).start()
        threading.Thread(target=lazy_populate_project_files, args=(self, )).start()

        # returning the root widget
        return container


def do():
    # Desktop Application
    if config["window-type"] == 'window':
        start(CircuitizerUI, standalone=True, width=1000, height=650)

    # Repl.it Web Application
    elif config["window-type"] == 'repl.it':
        start(CircuitizerUI, address='0.0.0.0', port=0)

    # Heroku Application
    elif config["window-type"] == 'heroku':
        start(CircuitizerUI, address='0.0.0.0', port=int(os.environ['PORT']), start_browser=False)
    
    # Browser Launch
    elif config["window-type"] == 'browser':
        start(CircuitizerUI)

    # True Desktop Application
    elif config["window-type"] == 'pure-desktop':
        PORT = 12313
        start(CircuitizerUI, address='127.0.0.1', port=PORT, start_browser=True)

# starts the web server
if __name__ == "__main__":
    do()
