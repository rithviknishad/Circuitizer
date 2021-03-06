#!/usr/bin/python3
# Circuitizer UI

import os
import glob
import json
import time
import threading

import remi.gui as gui
from remi import start, App

import UI.theme as theme
import UI.menuUI as menuUI
import UI.statusUI as statusUI
import UI.toolUI as toolUI

from UI.extras import *

# Load the configuration file for Circuitizer
config = json.load(open('UI/config.json'))
# Locate the resource folder
RES_PATH = './UI/resources/'


def lazy_populate_project_files(self_pointer, animate=True):
    time.sleep(1)
    self_pointer.project_list_canvas.empty()
    for file in glob.glob('*'):
        self_pointer.project_list_canvas.append(theme.EditorSelectionLink(text=file, animate=animate))


class CircuitizerUI(App):
    def __init__(self, *args):
        res_path = os.path.join(os.path.dirname(__file__), 'resources/remi')
        super(CircuitizerUI, self).__init__(*args, static_file_path = {'res':res_path, 'my_resources': RES_PATH, 'my_lib': RES_PATH + 'lib/'})
        """
        The Circuitizer Main UI
        """
        global pointer
        pointer = self
        self.load_stuff()
        # Load the status thread
        status_thread = threading.Thread(target=self.status_logic, args=())
        status_thread.daemon = True
        status_thread.start()

    def load_stuff(self):
        # Load no cache property to application
        # lazy_load_http_equiv(self)
        # Load library files
        for js in glob.glob(RES_PATH + 'lib/*.js'):
            lazy_load_js(self, "my_lib:" + os.path.basename(js))
        for css in glob.glob(RES_PATH + 'lib/*.css'):
            lazy_load_css(self, "my_lib:" + os.path.basename(css))
        # Load some local files
        for js in glob.glob(RES_PATH + '*.js'):
            lazy_load_js(self, "my_resources:" + os.path.basename(js))
        for css in glob.glob(RES_PATH + '*.css'):
            lazy_load_css(self, "my_resources:" + os.path.basename(css))
        # Load the material icons font
        lazy_load_css(self, "https://fonts.googleapis.com/icon?family=Material+Icons")
        

    def new_tab(self, file):
        print(file)

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

        ok_button = theme.EditorButton(text='Create', icon='add')

        def project_startup_page():
            self.canvas.empty()
            foo = gui.Label(project_name.get_text() + '.cxproj Project')
            foo.add_class('w3-jumbo')
            foo.style['height'] = '200px'
            foo.style['padding'] = '30px 30px 30px 30px'

            create_schematic_button = theme.EditorButton(text='Schematic', icon='edit')
            create_component_button = theme.EditorButton(text='Custom component definition', icon='edit')
            create_cppscript_button = theme.EditorButton(text='C++ Script', icon='edit')
            link_compiler_button = theme.EditorButton(text='Link custom compiler suite', icon='edit')
            lazy_populate_project_files(self, animate=False)

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
        try:
            self.status.set_text('Ready')
        except:
            print()
            # raise NotImplementedError('Waiting for Status bar to init')

    def panel_logic(self):
        self.properties_label = gui.Label(text="Properties Panel")
        self.properties_label.set_identifier('DragWidgetEditorPanelheader')
        self.properties_label.style['color'] = config["primary-foreground-color"]
        self.properties_label.style['display'] = 'table-row'
        self.properties_label.style['position'] = 'relative'
        self.properties_label.style['cursor'] = 'move'
        
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

        time.sleep(0.5)
        self.panel.style['width'] = gui.to_pix(int(config["panel-width"]))
        self.panel.add_class('w3-animate-right')

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
            top.append(theme.w3_dropdown_hover(text=menu, stuffs=MENUS[menu]))

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
        self.panel.set_identifier('DragWidgetEditorPanel')
        self.panel.style['position'] = 'absolute'
        self.panel.style['top'] = gui.to_pix(54)
        self.panel.style['z-index'] = str(2)
        self.panel.style['width'] = gui.to_pix(0)
        self.panel.style['right'] = str(0)
        self.panel.style['color'] = 'white'
        self.panel.style['height'] = '90%'
        self.panel.style['background-color'] = config["panel-background-color"]
        self.panel.style['padding'] = '10px 10px'

        # Enable resize property and resizer object
        self.panel.add_class('resizable resizers')
        self.panel_resizer = gui.Widget()
        self.panel_resizer.add_class('resizer top-left')
        self.panel_resizer.style['height'] = '5px'
        self.panel_resizer.style['width'] = '5px'
        self.panel_resizer.style['background-color'] = config["button-background-color"]
        self.panel_resizer.style['cursor'] = 'w-resize'
        self.panel.append(self.panel_resizer)

        container.append(self.panel)

        self.actionbar = gui.Widget()
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

        self.canvas.append(theme.EditorButton(text='Hi', icon='edit'))
        self.canvas.append(theme.SchematicEditor(self_pointer=self))

        container.append(self.canvas)

        self.status = statusUI.StatusUI(text='Please wait while background service is loading...')
        container.append(self.status)

        panel_logic_thread = threading.Thread(target=self.panel_logic, args=())
        panel_logic_thread.daemon = True
        panel_logic_thread.start()

        lazy_populate_project_files_thread = threading.Thread(target=lazy_populate_project_files, args=(self, ))
        lazy_populate_project_files_thread.daemon = True
        lazy_populate_project_files_thread.start()

        # returning the root widget
        return container

# Inject drag property to widgets
def inject_drag_property_to_widget_thread():
    global pointer
    # The property should exist when if the page is reloaded
    while True:
        time.sleep(3)
        inject_drag_property_to_widget(pointer, 'DragWidgetEditorProperty')
        inject_drag_property_to_widget_x_only(pointer, 'DragWidgetEditorPanel')

inject_drag_property_to_widget_threader = threading.Thread(target=inject_drag_property_to_widget_thread, args=())
inject_drag_property_to_widget_threader.daemon = True
inject_drag_property_to_widget_threader.start()

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
