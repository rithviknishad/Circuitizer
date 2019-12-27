#!/usr/bin/python3
import os
import json
import remi.gui as gui

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


class SchematicEditor(gui.Widget):
    pass

