import remi.gui as gui

MenuCSS = {
    'display' : 'table-cell',
    'color' : 'white',
    'text-align' : 'center',
    'background-color' : '#333',
    'padding' : '0px 9px',
    'text-decoration' : 'none',
    'top' : str(0),
    'color': '#969393',
    'height' : gui.to_pix(10),
    'position' : 'relative',
    'font-size' : gui.to_pix(13),
    'font-family': 'Helvetica'
}

class MenuUI(gui.Label):
    def __init__(self, **kwargs):
        super(MenuUI, self).__init__(**kwargs)
        self.set_style(MenuCSS)
