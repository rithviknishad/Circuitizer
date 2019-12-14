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

# custom imports

import crt
import libUI

from cfg import *


class Circuitizer:
    """Circuitizer UI Object"""
    def __init__(self, root):
        # The root reference
        self.root = root
        # A global pointer to self for accessing everywhere in the application
        global self_pointer
        self_pointer = self 
        # The toggle counter for the pen in the circuit canvaas
        self.toggle_pen = True

        # Basic Application Meta Data
        self.root.geometry(GEOMETERY)
        self.root.title("Circuitizer")
        self.root.configure(background=BG_COLOR)

        # This line will only work on win32 for some reason
        self.root.iconbitmap(RESOURCE_PATH + 'logo.ico' if 'win' in sys.platform else None)

        # The GUI components
        self.modern_menu_bar(root)
        self.tool_bar(root)
        self.status_bar(root)
        self.side_tool_bar(root)

        self.main_panel = tk.Frame(root)
        self.properties_panel(self.main_panel)
        self.project_panel(self.main_panel)
        self.main_panel.pack(side=tk.RIGHT, fill=tk.Y)

        self.main_content(root)

    def modern_menu_bar(self, root):
        """The menu div UI code"""
        self.frame = tk.Frame(root)
        self.frame.configure(background=TOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        def generate_ui(self, txt, icon=None, command=None):
            """Generate the UI with the custom theme"""
            self.open = tk.Button(self.frame, text=txt, relief=tk.FLAT, compound=tk.LEFT, highlightthickness=0)
            self.open.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            self.open.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5)

        # structure the ui
        for txt in ['File', 'Edit', 'Debug', 'Tools']:
            generate_ui(self, txt)

        self.frame.pack(fill=tk.X, side=tk.TOP)

    def tool_bar(self, root):
        """The tool bar UI code"""
        self.frame = tk.Frame(root)
        self.frame.configure(background=TOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        def generate_ui(self, icon, command=None):
            """Generate the UI with the custom theme"""
            self.image = tk.PhotoImage(file=icon)
            self.open = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, highlightthickness=0)
            self.open.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            self.open.image = self.image
            self.open.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5, ipady=5)

        # structure the ui
        for icon in glob.glob(os.getcwd() + '/resource/tool/*.png'):
            generate_ui(self, icon)

        self.frame.pack(fill=tk.X, side=tk.TOP)

    def properties_panel(self, root):
        """The properties panel div UI code"""
        self.frame = tk.Frame(root, width=200)
        self.frame.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        # The heading of the properties panel
        self.open = tk.Label(self.frame, text="Properties Panel                                                     ")
        self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR)
        self.open.pack(side=tk.TOP, fill=tk.BOTH, ipady=4)

        self.frame.pack(fill=tk.Y, side=tk.TOP, ipadx=10, ipady=3)
    
    def side_tool_bar(self, root):
        """The side tool bar div UI code"""
        self.frame = tk.Frame(root)
        self.frame.configure(background=SIDETOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        # The new button action
        def new_action(self):
            libUI.ComponentEditor(tk.Toplevel())
            crt_handler.realtime(self.pen.xcor(), self.pen.ycor(), 'and.gif')

        # The load button action
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

        def generate_ui(self, root, icon, command=None):
            """Generate the UI with the custom theme"""
            self.image = tk.PhotoImage(file=icon)
            self.add = tk.Button(self.frame, image=self.image, relief=tk.FLAT, compound=tk.LEFT, command=command, highlightthickness=0)
            self.add.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of image is required otherwise this image is garbage collected
            self.add.image = self.image
            self.add.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)

        # structure the ui
        for widget in [
            # The add button which can be used to add a new component to the schematic builder
            (ADD, None),
            # The draw button which can be used to draw the schematics in the schematic builder
            (ADD, None),
            # The new button can be used to build a new custom component for the schematic
            (ADD, lambda: new_action(self)),
            # The file button can be used to open a new schematic file to the editor
            (FILE, lambda: load_action(self)),
        ]:
            generate_ui(self, root, icon=widget[0], command=widget[1])

        self.frame.pack(fill=tk.Y, side=tk.LEFT, ipadx=10, ipady=3)
    
    def project_panel(self, root):
        global generate_tree
        """The project panel div UI code"""
        self.frame_panel = tk.Frame(root, width=200)
        self.frame_panel.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        def generate_tree(self, dir=os.getcwd()):
            # clean previous list
            for child in self.frame_panel.winfo_children():
                child.destroy()
            print(dir)
            # the heading of the project panel
            self.open = tk.Label(self.frame_panel, text="Project Files                                                          ")
            self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR)
            self.open.pack(side=tk.TOP, fill=tk.BOTH, ipadx=3, ipady=3)
            # load the current project working directory
            for file in glob.glob(dir + '/*'):
                if os.path.isdir(file):
                    self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/open.png').subsample(2, 2)
                    file = os.path.basename(file)
                else:
                    self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/file.png').subsample(2, 2)
                    file = os.path.basename(file)
                
                self.open = tk.Button(self.frame_panel, image=self.image, text="      " + file, anchor=tk.W, font=("Arial", 10), compound=tk.LEFT, highlightthickness=0, command=lambda: generate_tree(self, os.path.abspath(file)))
                self.open.image = self.image
                self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR, bd=0)
                self.open.pack(side=tk.TOP, fill=tk.BOTH, padx=20, ipady=3)

        self.frame_panel.pack(fill=tk.Y, side=tk.BOTTOM, ipadx=10, ipady=3)

        generate_tree(self)
        generate_tree(self)
    
    def main_content(self, root):
        """The main div UI code"""

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

        # Hide the canvas for now
        self.canvas.pack_forget()
        self.frame.pack(fill=tk.BOTH, side=tk.LEFT, ipadx=10, ipady=3)

    def status_bar(self, root):
        """The status bar UI code"""
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
    # Hide the windows before loading fully to prevent loading white flash in UI
    root.withdraw()
    # Circuitizer UI class bind to the root
    Circuitizer(root)
    # Unhide the window after it's fully loaded to show the window
    root.update()
    root.deiconify()
    root.mainloop()

if __name__ == "__main__":
    main()
