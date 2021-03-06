import remi.gui as gui

StatusCSS = {
    'color' : 'white',
    'text-align' : 'left',
    'background-color' : '#e3a42c',
    'text-decoration' : str(None),
    'bottom' : str(0),
    'width' : '100%',
    'height' : gui.to_pix(22),
    'position' : 'fixed',
    'font-size' : 'small',
    'overflow' : 'hidden',
    'z-index': str(3)
}

class StatusUI(gui.Label):
    def __init__(self, **kwargs):
        super(StatusUI, self).__init__(**kwargs)
        self.set_style(StatusCSS)
