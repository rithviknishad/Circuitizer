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
    def __init__(self, text, function=None, **kwargs):
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
                self.add_class('w3-animate-right w3-button')

        class MaterialIcon(gui.Label):
            def __init__(self, **kwargs):
                super(MaterialIcon, self).__init__(**kwargs)
                self.type = 'i'
                self.style['font-size'] = 'small'
                self.style['padding'] = gui.to_pix(4)
                self.add_class('material-icons w3-animate-zoom')

        self.append(MaterialIcon(text='note_add'))
        if not os.path.isfile(os.path.abspath(text)):
            self.empty()
            self.append(MaterialIcon(text='folder'))

        self.button = LinkText(text=text)
        self.button.onclick.do(function)
        self.append(self.button)

