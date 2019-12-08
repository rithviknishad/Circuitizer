#!/usr/bin/python3
# Circuitizer Component UI

import os
import sys
import glob
import ctypes

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkdialog

# custom imports

from cfg import *


class ComponentEditor:
    def __init__(self, root):
        # The root reference
        self.root = root

        # Basic Application Meta Data
        self.root.title('Component Editor')
        self.root.geometry("800x500")
        self.root.configure(background=BG_COLOR)

        # The GUI components
        self.tool_bar(root)
        self.content(root)
        self.status_bar(root)
    
    def content(self, root):
        """The content div UI code"""
        self.frame = tk.Frame(root)
        # The image preview canvas
        self.img_frame = tk.Frame(self.frame)
        self.img_frame.configure(background=BG_COLOR)
        self.img = tk.Label(self.img_frame, width=300, height=415, image=self.image, relief=tk.FLAT, compound=tk.LEFT, background=BG_COLOR)
        self.img.pack(fill=tk.BOTH)
        self.img_frame.pack(side=tk.LEFT)
    
        # The definitions of components
        self.detail_frame = tk.Frame(self.frame, background=BORDER_COLOR)

        # Properties of the components are give below after this label
        self.tmp_frame = tk.Frame(self.detail_frame, background=BORDER_COLOR)
        self.temp = tk.Label(self.tmp_frame, text="    Properties Panel \t\t\t\t\t\t\n", background=BORDER_COLOR, foreground=FG_COLOR)
        self.temp.pack(side=tk.LEFT)
        self.tmp_frame.pack(side=tk.TOP)

        # Name of the symbols
        self.name_frame = tk.Frame(self.detail_frame, background=BORDER_COLOR)
        self.temp = tk.Label(self.name_frame, text="    Component \t\t", background=BORDER_COLOR, foreground='white')
        self.temp.pack(side=tk.LEFT)
        self.name = tk.Entry(self.name_frame, width=30)
        self.name.pack(side=tk.RIGHT)
        self.name_frame.pack(side=tk.TOP, pady=4)

        # Placeholder of the symbols
        self.placeholder_frame = tk.Frame(self.detail_frame, background=BORDER_COLOR)
        self.temp = tk.Label(self.placeholder_frame, text="    Placeholder\t\t", background=BORDER_COLOR, foreground='white')
        self.temp.pack(side=tk.LEFT)
        self.placeholder = tk.Entry(self.placeholder_frame, width=30)
        self.placeholder.pack(side=tk.RIGHT)
        self.placeholder_frame.pack(side=tk.BOTTOM, pady=4)

        # Max Volt of the symbols
        self.max_volt_frame = tk.Frame(self.detail_frame, background=BORDER_COLOR)
        self.temp = tk.Label(self.max_volt_frame, text="    Max Volt\t\t", background=BORDER_COLOR, foreground='white')
        self.temp.pack(side=tk.LEFT)
        self.max_volt = tk.Entry(self.max_volt_frame, width=30)
        self.max_volt.pack(side=tk.RIGHT)
        self.max_volt_frame.pack(side=tk.BOTTOM, pady=4)

        self.detail_frame.pack(side=tk.LEFT)
        self.frame.configure(background=BORDER_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH)

    def tool_bar(self, root):
        """The tool bar UI code"""
        self.frame = tk.Frame(root)
        self.frame.configure(background=TOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        # the add component action which will load the symbol to the image preview div
        def add_component(self):
            img_file = tkdialog.askopenfilename(filetypes=(
                        ("GIF files", "*.gif"),
                        ("PNG files", "*.png"),
                        ("All files", "*.*")
                    )
                )
            if img_file is not None:
                self.image = tk.PhotoImage(file=img_file)
                self.img.config(image=self.image)
                self.img.image = self.image
                print(img_file)

        def generate_ui(self, icon, command):
            """Generate the UI with the custom theme"""
            self.image = tk.PhotoImage(file=icon)
            self.open = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, command=command)
            self.open.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.open.image = self.image
            self.open.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5, ipady=5)

        # structure of ui
        for widget in [
            (ADD, lambda: add_component(self)),
            (CARD, None), (CLOUD, None)
        ]:
            generate_ui(self, icon=widget[0], command=widget[1])

        self.frame.pack(fill=tk.X, side=tk.TOP)
    
    def status_bar(self, root):
        """The status bar UI code"""
        # render the frame for the status bar
        self.frame = tk.Frame(root)
        self.frame.configure(background=STATUS_COLOR)

        # the status text with some status information
        self.txt = tk.Label(self.frame, text="Latest Version")
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
    ComponentEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
