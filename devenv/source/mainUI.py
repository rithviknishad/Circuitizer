#!/usr/bin/python3
# Circuitizer UI

import os
import gc
import sys
import glob
import time
import ctypes
import threading

import tkinter as tk
import tkinter.filedialog as tkdialog

# custom imports

import crt
import libcom
import libtreeUI

from cfg import GEOMETERY, BG_COLOR, FG_COLOR, PANEL_COLOR, STATUS_COLOR, \
    BORDER_COLOR, TOOL_COLOR, SIDETOOL_COLOR, PEN_COLOR, ADD, CARD, CLOUD, \
    FILE, GRAPH, MONEY, REFRESH, SAVE, SETTINGS, RESOURCE_PATH, COMPONENT_PATH, \
    THREAD_RESPONSE_RATE, TAB_POS


class Circuitizer:
    """Circuitizer UI Object"""
    def __init__(self, root):
        # The root reference
        self.root = root
        # A global pointer to self for accessing everywhere in the application
        global self_pointer
        self_pointer = self

        # Basic Application Meta Data
        self.root.geometry(GEOMETERY)
        self.root.title("Circuitizer")
        self.root.configure(background=BG_COLOR)
        self.root.protocol("WM_DELETE_WINDOW", self.ui_onquit)

        # This line will only work on win32 for some reason
        self.root.iconbitmap(RESOURCE_PATH + 'logo.ico' if 'win' in sys.platform else None)

        # The tab's close icon
        self.close_icon_tab = tk.PhotoImage(file=os.getcwd() + '/resource/tool/close.png').subsample(2, 2)

        # The GUI components
        self.modern_menu_bar(root)
        self.tool_bar(root)
        self.status_bar(root)
        self.side_tool_bar(root)

        self.main_panel = tk.Frame(root, background=PANEL_COLOR, highlightthickness=0)
        self.properties_panel(self.main_panel)
        self.project_panel(self.main_panel)
        self.main_panel.pack(side=tk.RIGHT, fill=tk.Y)

        self.main_content(root)

    def ui_onquit(self):
        global exitFlag
        exitFlag = True
        self.root.destroy()

    def modern_menu_bar(self, root):
        """The menu div UI code"""
        self.frame = tk.Frame(root)
        self.frame.configure(background=TOOL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        def generate_ui(self, txt, icon=None, command=None):
            """Generate the UI with the custom theme"""
            open = tk.Button(self.frame, text=txt, relief=tk.FLAT, compound=tk.LEFT, highlightthickness=0, bd=0, highlightcolor=BORDER_COLOR)
            open.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            open.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5)
            open.bind("<Enter>", lambda x: open.configure(background=PANEL_COLOR))
            open.bind("<Leave>", lambda x: open.configure(background=TOOL_COLOR))

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
            open = tk.Button(self.frame, image=self.image, bd=0, relief=tk.FLAT, compound=tk.LEFT, highlightthickness=0)
            open.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of this image is required otherwise this image is garbage collected
            open.image = self.image
            open.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5, ipady=5)
            open.bind("<Enter>", lambda x: open.configure(background=PANEL_COLOR))
            open.bind("<Leave>", lambda x: open.configure(background=TOOL_COLOR))

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
            add = tk.Button(self.frame, image=self.image, bd=0, relief=tk.FLAT, compound=tk.LEFT, command=command, highlightthickness=0)
            add.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of image is required otherwise this image is garbage collected
            add.image = self.image
            add.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)
            add.bind("<Enter>", lambda x: add.configure(background=PANEL_COLOR))
            add.bind("<Leave>", lambda x: add.configure(background=TOOL_COLOR))

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
        """The project panel div UI code"""
        self.frame = tk.Frame(root)
        self.frame.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        self.panel = libtreeUI.PanelTree(self.frame, panel_width=100)
        self.panel.refresh()
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.NO)
        self.open = tk.Label(self.frame, text="Project Files", anchor='nw')
        self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        self.open.pack(side=tk.BOTTOM, fill=tk.BOTH, ipady=3, padx=10, pady=3)
        self.frame.pack(fill=tk.BOTH, side=tk.BOTTOM, ipadx=10, ipady=3, expand=True)

    def main_content(self, root):
        """The main div UI code"""
        # The main frame where the circuit canvas is rendered
        self.main = libtreeUI.TabTree(root, panel_width=None)
        self.main.scrollFrame.vsb.pack_forget()
        self.main.configure(background=BG_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)

        def add_tab(self, name):
            self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/file.png').subsample(2, 2)
            add = tk.Button(self.main.scrollFrame.viewPort, text='    ' + name, image=self.image, bd=0, relief=tk.FLAT, compound=tk.LEFT, highlightthickness=0)
            add.configure(background=TOOL_COLOR, foreground=FG_COLOR)

            def close_tab():
                add.forget()
                close.forget()
            close = tk.Button(self.main.scrollFrame.viewPort, image=self.close_icon_tab, bd=0, relief=tk.FLAT, compound=tk.RIGHT, highlightthickness=0, command=close_tab)
            close.configure(background=TOOL_COLOR, foreground=FG_COLOR)
            # reference of image is required otherwise this image is garbage collected
            add.image = self.image
            add.pack(side=tk.LEFT, fill=tk.BOTH, ipady=5, ipadx=10)
            close.pack(side=tk.LEFT, fill=tk.BOTH, ipady=5, ipadx=10)
            add.bind("<Enter>", lambda x: add.configure(background=PANEL_COLOR))
            add.bind("<Leave>", lambda x: add.configure(background=TOOL_COLOR))

        self.main.pack(fill=tk.BOTH, side=TAB_POS, ipadx=30)

        add_tab(self, "Blank")

        def libcom_analyse_thread(self_pointer, add_tab_func_signature, exitflag_signature, THREAD_RESPONSE_RATE_signature):
            while True:
                # The thread response delay
                time.sleep(THREAD_RESPONSE_RATE)
                # Auto enable scrollbar for tabs if it fills the space
                if self.main.scrollFrame.viewPort.winfo_width() > self.main.winfo_width():
                    self.main.scrollFrame.vsb.pack(side="right", fill="both")
                else:
                    self.main.scrollFrame.vsb.pack_forget()
                # Add new tab if CurrentTab value is changed
                if (libcom.CurrentTab.value is not None):
                    if not os.path.isdir(os.path.abspath(libcom.CurrentTab.value)):
                        add_tab_func_signature(self_pointer, libcom.CurrentTab.value)
                        libcom.CurrentTab.reset()
                # Exit condition for the thread
                if exitFlag:
                    break
        threading.Thread(target=lambda: libcom_analyse_thread(self, add_tab, exitFlag, THREAD_RESPONSE_RATE)).start()

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
    # Some global variable which are assigned with values later
    crt_handler, self_pointer, generate_tree, exitFlag = None, None, None, False
    # Call main function
    main()
