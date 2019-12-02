import os
import sys
import glob
import ctypes

import tkinter as tk
import tkinter.ttk as ttk

from config import *

class ComponentEditor:
    def __init__(self, root):
        self.root = root
        self.root.title('Component Editor')
        self.root.geometry("800x500")
        self.root.configure(background=BG_COLOR)
        self.tool_bar(root)
        self.status_bar(root)
    
    def tool_bar(self, root):
        self.frame = tk.Frame(root)
        self.frame.configure(background=TOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        def generate_tools(self, icon, command):
            self.image = tk.PhotoImage(file=icon)
            self.open = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT)
            self.open.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.open.image = self.image
            self.open.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5, ipady=5)

        for icon in [ADD, CARD, CLOUD]:
            generate_tools(self, tk.PhotoImage(file=os.getcwd() + icon), None)

        self.frame.pack(fill=tk.X, side=tk.TOP)
    
    def status_bar(self, root):
        self.frame = tk.Frame(root)
        self.frame.configure(background=STATUS_COLOR)

        self.txt = tk.Label(self.frame, text="Latest Version")
        self.txt.configure(background=STATUS_COLOR, foreground='white')
        self.txt.pack(side=tk.LEFT)

        self.frame.pack(fill=tk.X, side=tk.BOTTOM)

if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Toplevel()
    ComponentEditor(root)
    root.mainloop()
