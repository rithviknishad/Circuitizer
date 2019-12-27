#!/usr/bin/python3
import json
import remi.gui as gui

config = json.load(open('UI/config.json'))


class EditorButton(gui.Label):
    def __init__(self, icon, **kwargs):
        super(EditorButton, self).__init__(**kwargs)
        self.type = 'a'
        self.style['font-family'] = 'Roboto'
        self.add_class('w3-button waves-effect waves-light')
        self.style['background-color'] = config["button-background-color"]
        class MaterialIcon(gui.Label):
            def __init__(self, **kwargs):
                super(MaterialIcon, self).__init__(**kwargs)
                self.type = 'i'
                self.style['font-size'] = 'small'
                self.style['padding'] = gui.to_pix(4)
                self.add_class('material-icons')
        self.append(MaterialIcon(text=icon))
