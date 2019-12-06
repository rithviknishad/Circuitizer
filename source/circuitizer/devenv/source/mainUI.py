#!/usr/bin/python3
# Circuitizer UI

import os
import gc
import sys
import glob
import ctypes
import turtle

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkdialog

sys.dont_write_bytecode = True

from cfg import *

import crt
import libUI

class Circuitizer:
    """Circuitizer UI Object"""
    def __init__(self, root):
        # The root reference
        self.root = root
        # The toggle counter for the pen in the circuit canvaas
        self.toggle_pen = True
        self.filename = None
        self.temp_filename = 'working.circuit'
        # Clean the working circuit file
        # self.clean_realtime_crt()
        # Basic Application Meta Data
        self.root.geometry("1200x700")
        self.root.title("Circuitizer")
        self.root.configure(background=BG_COLOR)
        # The GUI components
        self.menu_bar(root)
        self.tool_bar(root)
        self.status_bar(root)
        self.properties_panel(root)
        self.side_tool_bar(root)
        self.project_panel(root)
        self.main_content(root)

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

        for icon in glob.glob(os.getcwd() + '/resource/tool/*.png'):
            generate_tools(self, icon, None)

        self.frame.pack(fill=tk.X, side=tk.TOP)

    def properties_panel(self, root):
        self.frame = tk.Frame(root, width=200)
        self.frame.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        self.open = tk.Label(self.frame, text="Properties Panel                                                     ")
        self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR)
        self.open.pack(side=tk.TOP, fill=tk.BOTH, ipady=4)

        self.frame.pack(fill=tk.Y, side=tk.RIGHT, ipadx=10, ipady=3)
    
    class Events:
        def draw_button_event(self):
            if self.toggle_pen:
                self.pen.down()
                self.toggle_pen = False
            else:
                self.pen.up()
                self.toggle_pen = True

    def side_tool_bar(self, root):
        self.frame = tk.Frame(root)
        self.frame.configure(background=SIDETOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        class ADD_BUTTON:
            self.image = tk.PhotoImage(file=ADD)
            self.add = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, command=None)
            self.add.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.add.image = self.image
            self.add.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)
    
        class DRAW_BUTTON:
            self.image = tk.PhotoImage(file=ADD)
            self.add = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, command=lambda: exec("self_pointer.Events.draw_button_event(self_pointer)"))
            self.add.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.add.image = self.image
            self.add.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)

        class NEW_BUTTON:
            global new_action
            def new_action(self):
                libUI.ComponentEditor(tk.Toplevel())
                crt_handler.realtime(self.pen.xcor(), self.pen.ycor(), 'and.gif')
            self.image = tk.PhotoImage(file=ADD)
            self.add = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, command=lambda: new_action(self))
            self.add.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.add.image = self.image
            self.add.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)
        
        class LOAD_BUTTON:
            global load_action
            def load_action(self):
                file = tkdialog.askopenfilename(filetypes=(
                        ("Circuit files", "*.circuit"),
                        ("Schematic files", "*.schematic"),
                        ("Definition files", "*.definition"),
                        ("Realtime Circuit File", "working.circuit"),
                        ("All files", "*.*")
                    )
                )
                if file is not None:
                    exec(''.join(crt_handler.load(crt_handler.work)[0]))
            self.image = tk.PhotoImage(file=FILE)
            self.load = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, command=lambda: load_action(self))
            self.load.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.load.image = self.image
            self.load.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)

        self.frame.pack(fill=tk.Y, side=tk.LEFT, ipadx=10, ipady=3)
    
    def clean_realtime_crt(self):
        file = open(self.temp_filename, 'w')
        file.write('')
        file.close()

    def realtime_save_crt(self, x, y):
        self.pen.stamp()
        self.pen.goto(x - 10, y - 10)
        file = open(self.temp_filename, 'a')
        file.write('\nself.pen.goto(' + str(x) + ',' + str(y) + ')')
        file.write('\nself.pen.stamp()')
        file.close()

    def project_panel(self, root):
        self.frame = tk.Frame(root)
        self.frame.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        self.open = tk.Label(self.frame, text="Project Files                          ")
        self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR)
        self.open.pack(side=tk.TOP, fill=tk.BOTH, ipadx=3, ipady=3)
        
        for file in glob.glob('*'):
            if os.path.isdir(file):
                self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/open.png').subsample(2, 2)
            else:
                self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/file.png').subsample(2, 2)
            self.open = tk.Button(self.frame, image=self.image, text="      " + file, anchor=tk.W, font=("Arial", 10), compound=tk.LEFT)
            self.open.image = self.image
            self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR, bd=0)
            self.open.pack(side=tk.TOP, fill=tk.BOTH, padx=20, ipady=3)

        self.frame.pack(fill=tk.Y, side=tk.LEFT, ipadx=10, ipady=3)
    
    def main_content(self, root):
        # A global pointer to self for accessing everywhere in the application
        global self_pointer
        self_pointer = self 
        # The main frame where the circuit canvas is rendered
        self.frame = tk.Frame(root)
        self.frame.configure(background=BG_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        self.canvas = turtle.ScrolledCanvas(root, canvwidth=2000, canvheight=2000)
        # Pen configuration
        self.pen = turtle.RawTurtle(self.canvas)
        self.pen.color(PEN_COLOR)
        self.pen.speed(5)
        self.pen.shapesize(1.5)
        self.pen.shape('circle')
        self.pen.setundobuffer(1000)
        self.pen.up()
        # left button of mouse to drag the cursor of the canvas
        self.pen.ondrag(self.pen.goto)
        self.canvas.config(background=BG_COLOR, highlightthickness=0, highlightbackground=BORDER_COLOR)
        # middle button of mouse to drag canvas
        self.canvas.bind("<ButtonPress-2>", lambda event: self.canvas.scan_mark(event.x, event.y))
        self.canvas.bind("<B2-Motion>", lambda event: self.canvas.scan_dragto(event.x, event.y, gain=1))
        self.canvas.pack(fill=tk.BOTH, expand=True)
        # self.canvas.destroy()
        self.frame.pack(fill=tk.BOTH, side=tk.LEFT, ipadx=10, ipady=3)

    def status_bar(self, root):
        # render the frame for the status bar
        self.frame = tk.Frame(root)
        self.frame.configure(background=STATUS_COLOR)
        # the status text with some status information
        self.txt = tk.Label(self.frame, text="Ready")
        self.txt.configure(background=STATUS_COLOR, foreground='white')
        self.txt.pack(side=tk.LEFT)
        self.frame.pack(fill=tk.X, side=tk.BOTTOM)


def main():
    global crt_handler
    # Fix text blurry issue in windows 10 due to text scale settings
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # The turtle drag and drop function rescursion is more than python's standard limit
    sys.setrecursionlimit(10000)
    # Disable garbage collector for better performance
    gc.disable()
    # Circuit handler which will be used to do I/O in .circuit files
    crt_handler = crt.Circuit()
    # Init the tkinter GUI process
    root = tk.Tk()
    Circuitizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
