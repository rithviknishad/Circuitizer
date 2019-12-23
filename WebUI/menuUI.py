import remi.gui as gui

MenuCSS = {
    'display' : 'table-cell',
    'text-align' : 'center',
    'background-color' : '#302d2d',
    'padding' : '0px 9px',
    'text-decoration' : 'none',
    'top' : str(0),
    'color': '#969393',
    'height' : gui.to_pix(10),
    'position' : 'relative',
    'font-size' : gui.to_pix(13),
    'font-family': gui.to_uri('fa-regular-400.wooff')
}

class MenuUI(gui.Label):
    def __init__(self, **kwargs):
        super(MenuUI, self).__init__(**kwargs)
        self.set_style(MenuCSS)
