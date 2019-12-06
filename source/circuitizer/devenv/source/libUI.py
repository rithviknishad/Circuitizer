import os
import sys
import glob
import ctypes

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkdialog

from cfg import *

class ComponentEditor:
    def __init__(self, root):
        self.root = root
        self.root.title('Component Editor')
        self.root.geometry("800x500")
        self.root.configure(background=BG_COLOR)
        self.tool_bar(root)
        self.content(root)
        self.status_bar(root)
    
    def content(self, root):
        self.frame = tk.Frame(root)
        self.img_frame = tk.Frame(self.frame)
        self.img = tk.Label(self.img_frame, width=300, height=415, image=self.image, relief=tk.FLAT, compound=tk.LEFT)
        self.img.pack(fill=tk.BOTH)
        self.img_frame.grid(row=0, column=1)
        self.frame.configure(background=BORDER_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH)

    def tool_bar(self, root):
        self.frame = tk.Frame(root)
        self.frame.configure(background=TOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        def generate_tools(self, icon, command):
            self.image = tk.PhotoImage(file=icon)
            self.open = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, command=command)
            self.open.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.open.image = self.image
            self.open.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5, ipady=5)

        def add_component(self):
            file = tkdialog.askopenfilename(filetypes=(
                        ("Gif files", "*.gif"),
                        ("All files", "*.*")
                    )
                )
            if file is not None:
                self.img_frame.image = file
                print(file)
        generate_tools(self, ADD, lambda: add_component(self))
        generate_tools(self, CARD, None)
        generate_tools(self, CLOUD, None)
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
