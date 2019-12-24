import remi.gui as gui

ToolCSS = {
    'display' : 'table-cell',
    'text-align' : 'center',
    'background-color' : '#333',
    'padding' : '0px 9px',
    'text-decoration' : 'none',
    'top' : str(0),
    'color': '#969393',
    'height' : gui.to_pix(30),
    'position' : 'relative',
    'font-size' : gui.to_pix(15),
    'font-family': gui.to_uri('my_resources:fa-regular-400.wooff')
}

class ToolUI(gui.Label):
    def __init__(self, **kwargs):
        super(ToolUI, self).__init__(**kwargs)
        self.set_style(ToolCSS)
