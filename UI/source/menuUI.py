import sys
import ctypes

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkdialog

# custom imports

from cfg import *


class MenuUI:
    def __init__(self, root):
        # The root reference
        self.root = root
        self.root.overrideredirect(True)
        self.root.configure(background=BG_COLOR)

    def file_menu(self, root):
        self.new = tk.Button(root, text="New Project", )

def main():
    # Fix text blurry issue in windows 10 due to text scale settings
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # Init the tkinter GUI process
    root = tk.Toplevel()
    # Circuitizer Component UI class bind to the root
    MenuUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
