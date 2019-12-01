#!/usr/bin/python3

import sys
import tkinter as tk

BG_COLOR = "white"

class Circuitizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Circuitizer")
        self.root.configure(background=BG_COLOR)
        self.menu_bar(root)
        self.status_bar(root)

    def menu_bar(self, root):
        self.menubar = tk.Menu(root)
        self.root.config(menu=self.menubar)

        class FileMenu:
            self.filemenu = tk.Menu(self.menubar, tearoff=0)

            self.filemenu.add_command(label="New", command=None)
            self.filemenu.add_command(label="Open", command=None)
            self.filemenu.add_command(label="Save", command=None)
            self.filemenu.add_command(label="Save as...", command=None)
            self.filemenu.add_command(label="Close", command=None)

            self.filemenu.add_separator()

            self.filemenu.add_command(label="Exit", command=root.quit)

            self.menubar.add_cascade(label="File", menu=self.filemenu)

        class EditMenu:
            self.editmenu = tk.Menu(self.menubar, tearoff=0)

            self.editmenu.add_command(label="Undo", command=None)
            self.editmenu.add_command(label="Redo", command=None)

            self.editmenu.add_separator()

            self.editmenu.add_command(label="Cut", command=None)
            self.editmenu.add_command(label="Copy", command=None)
            self.editmenu.add_command(label="Paste", command=None)
            self.editmenu.add_command(label="Delete", command=None)
            self.editmenu.add_command(label="Select All", command=None)

            self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        class HelpMenu:
            self.helpmenu = tk.Menu(self.menubar, tearoff=0)
    
            self.helpmenu.add_command(label="Help Index", command=None)
            self.helpmenu.add_command(label="About...", command=None)
    
            self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    def properties_panel(self, root):
        pass

    def project_panel(self, root):
        pass

    def status_bar(self, root):
        self.frame = tk.Frame(root)
        self.frame.configure(background=BG_COLOR)

        self.txt = tk.Label(self.frame, text="Ready")
        self.txt.configure(background=BG_COLOR)
        self.txt.pack(side=tk.LEFT)

        self.frame.pack(fill=tk.X, side=tk.BOTTOM)

if __name__ == "__main__":
    root = tk.Tk()
    Circuitizer(root)
    root.mainloop()
