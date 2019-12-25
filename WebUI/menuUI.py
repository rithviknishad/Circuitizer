import remi.gui as gui

MenuCSS = {
    'text-align' : 'center',
    'background-color' : '#302d2d',
    'padding' : '0px 8px',
    'text-decoration' : 'none',
    'top' : str(0),
    'color': '#969393',
    'position' : 'relative',
    'font-size' : gui.to_pix(13),
    # 'font-family': gui.to_uri('my_resources:fa-regular-400.wooff')
}

class MenuUI(gui.Label):
    def __init__(self, **kwargs):
        super(MenuUI, self).__init__(**kwargs)
        self.set_style(MenuCSS)
