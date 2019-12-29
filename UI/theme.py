#!/usr/bin/python3
import os
import glob
import json
import threading
import remi.gui as gui

from UI.extras import inject_drag_property_to_widget

config = json.load(open('UI/config.json'))


class EditorButton(gui.Label):
    def __init__(self, icon, **kwargs):
        super(EditorButton, self).__init__(**kwargs)
        self.type = 'a'
        self.style['font-family'] = 'Roboto'
        self.style['border-radius'] = gui.to_pix(4)
        self.style['background-color'] = config["button-background-color"]
        self.style['color'] = config["primary-foreground-color"]
        self.add_class('bounceIn w3-button')

        class MaterialIcon(gui.Label):
            def __init__(self, **kwargs):
                super(MaterialIcon, self).__init__(**kwargs)
                self.type = 'i'
                self.style['font-size'] = 'small'
                self.style['padding'] = gui.to_pix(4)
                self.add_class('material-icons')

        self.append(MaterialIcon(text=icon))


class EditorSelectionLink(gui.Widget):
    def __init__(self, text, animate=True, function=None, **kwargs):
        super(EditorSelectionLink, self).__init__(**kwargs)
        self.style['display'] = 'table-row'
        self.style['text-align'] = 'left'
        self.style['background-color'] = config["panel-background-color"]

        class LinkText(gui.Label):
            def __init__(self, **kwargs):
                super(LinkText, self).__init__(**kwargs)
                self.type = 'a'
                self.style['font-family'] = 'Roboto'
                self.style['background-color'] = config["panel-background-color"]
                self.style['color'] = config["primary-foreground-color"]
                if animate:
                    self.add_class('w3-animate-right w3-button')
                else:
                    self.add_class('w3-button')

        class MaterialIcon(gui.Label):
            def __init__(self, **kwargs):
                super(MaterialIcon, self).__init__(**kwargs)
                self.type = 'i'
                self.style['font-size'] = 'small'
                self.style['padding'] = gui.to_pix(4)
                if animate:
                    self.add_class('material-icons w3-animate-zoom')
                else:
                    self.add_class('material-icons')

        self.append(MaterialIcon(text='note_add'))
        if not os.path.isfile(os.path.abspath(text)):
            self.empty()
            self.append(MaterialIcon(text='folder'))

        self.button = LinkText(text=text)
        self.button.onclick.do(function)
        self.append(self.button)

import UI.menuUI as menuUI

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

                self.add_class('bounceIn w3-button')
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
                        self.style['padding'] = gui.to_pix(int(config['dropbox-item-padding']))
                        self.add_class('w3-bar-item w3-button w3-animate-left')
                        self.onclick.do(event)

                for key in items:
                    global event
                    event = items[key]
                    self.append(item(text=key))

        self.append(w3_dropdown_content())


class EditorActionBarButton(gui.Label):
    def __init__(self, **kwargs):
        super(EditorActionBarButton, self).__init__(**kwargs)
        self.type = 'i'
        self.style['color'] = config["primary-foreground-color"]
        self.style['padding'] = '5px 8px'
        self.add_class('material-icons w3-button')


class ComponentImporter(gui.Widget):
    def __init__(self, self_pointer, **kwargs):
        super(ComponentImporter, self).__init__(**kwargs)
        self_pointer.canvas.empty()
        self_pointer.canvas.append(gui.Label('Component Importer'))
        self.component_list = gui.ListView()
        self.lazy_load_component_list(self_pointer)
        self_pointer.canvas.append(EditorButton(text='Import', icon='add'))

    def lazy_load_component_list(self, self_pointer):
        for i in glob.glob('Components/*.symbol'):
            component = gui.ListItem(i)
            component.onclick.do(lambda e: self.deploy_component(self_pointer, e.get_text()))
            self.component_list.append(component)
        self_pointer.canvas.append(self.component_list)

    def deploy_component(self, self_pointer, text):
        self_pointer.canvas.empty()
        component_widget = gui.Widget()
        
        component_widget.set_identifier('DeployedWidget')
        component_widget.style['width'] = gui.to_pix(40)
        component_widget.style['height'] = gui.to_pix(40)
        component_widget.style['position'] = 'absolute'

        inside = gui.Label(text=text)
        inside.style['background-color'] = '#2196F3'
        inside.style['cursor'] = 'move'
        inside.set_identifier(component_widget.identifier + 'header')
        component_widget.append(inside)

        self_pointer.canvas.append(component_widget)


class SchematicEditor(gui.Widget):
    def __init__(self, self_pointer, **kwargs):
        super(SchematicEditor, self).__init__(**kwargs)
        self_pointer.canvas.empty()

        def add_component_button_event(event):
            return ComponentImporter(self_pointer=self_pointer)

        add_component_button = EditorActionBarButton(text='add')
        add_component_button.onclick.do(add_component_button_event)
        self_pointer.actionbar.append(add_component_button)

        component_widget = gui.Widget()
        component_widget.set_identifier('DragWidgetEditorProperty')
        component_widget.style['width'] = gui.to_pix(40)
        component_widget.style['height'] = gui.to_pix(40)
        component_widget.style['position'] = 'absolute'

        inside = gui.Label(text='Hi')
        inside.style['background-color'] = '#2196F3'
        inside.style['cursor'] = 'move'
        inside.set_identifier(component_widget.identifier + 'header')
        component_widget.append(inside)

        self_pointer.canvas.append(component_widget)

