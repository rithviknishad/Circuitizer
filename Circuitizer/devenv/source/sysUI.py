# Circuitizer Settings UI

import sys
import ctypes

import tkinter as tk
import tkinter.ttk as ttk

from cfg import *


class CircuitizerSettings:
    """Circuitizer Settings UI Object"""
    def __init__(self, root):
        # The root reference
        self.root = root

        # Basic Application Meta Data
        self.root.geometry(GEOMETERY)
        self.root.title("Settings")
        self.root.configure(background=BG_COLOR)

        # This line will only work on win32 for some reason
        self.root.iconbitmap(RESOURCE_PATH + 'logo.ico' if 'win' in sys.platform else None)

        # The GUI components
        self.status_bar(root)

    def status_bar(self, root):
        """The status bar UI code"""
        # render the frame for the status bar
        self.frame = tk.Frame(root)
        self.frame.configure(background=STATUS_COLOR)

        # the status text with some status information
        self.txt = tk.Label(self.frame, text="")
        self.txt.configure(background=STATUS_COLOR, foreground='white')
        self.txt.pack(side=tk.LEFT)
        self.frame.pack(fill=tk.X, side=tk.BOTTOM)


def main():
    # Fix text blurry issue in windows 10 due to text scale settings
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # Init the tkinter GUI process
    root = tk.Toplevel()
    # Circuitizer Component UI class bind to the root
    CircuitizerSettings(root)
    root.mainloop()

if __name__ == "__main__":
    main()
