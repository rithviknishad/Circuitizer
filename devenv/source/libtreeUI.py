# ************************
# Scrollable Frame Class
# ************************

import os
import glob
import tkinter as tk

from cfg import GEOMETERY, BG_COLOR, FG_COLOR, PANEL_COLOR, STATUS_COLOR, \
    BORDER_COLOR, TOOL_COLOR, SIDETOOL_COLOR, PEN_COLOR, ADD, CARD, CLOUD, \
    FILE, GRAPH, MONEY, REFRESH, SAVE, SETTINGS, RESOURCE_PATH, COMPONENT_PATH


class ScrollFrame(tk.Frame):
    def __init__(self, parent, *args, **kw):
        super().__init__(parent, *args, **kw)
        self.panel_width = None

    def construct(self):
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=self.panel_width)
        self.canvas.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        self.viewPort = tk.Frame(self.canvas, highlightthickness=0, width=self.panel_width)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.viewPort, anchor="nw", tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

        self.onFrameConfigure(None)

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)


class PanelTree(tk.Frame):
    def __init__(self, root, panel_width):
        tk.Frame.__init__(self, root)
        global generate_tree_project_view
        self.scrollFrame = ScrollFrame(self)
        self.scrollFrame.panel_width = panel_width
        self.scrollFrame.construct()
        self.scrollFrame.viewPort.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=0)

        def generate_tree_project_view(self, dir=os.getcwd()):
            row = 0
            # clean previous list
            for child in self.scrollFrame.viewPort.winfo_children():
                child.destroy()
            print(dir)
            # the heading of the project panel
            tk.Label(self.scrollFrame.viewPort, background=PANEL_COLOR).grid(row=row)
            # load the current project working directory
            for file in glob.glob(dir + '/*'):
                row += 1
                if os.path.isdir(file):
                    self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/open.png').subsample(2, 2)
                    file = os.path.basename(file)
                else:
                    self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/file.png').subsample(2, 2)
                    file = os.path.basename(file)
                # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
                self.open_frame = tk.Frame(self.scrollFrame.viewPort)
                self.open_frame.configure(background=PANEL_COLOR)
                self.open = tk.Button(self.open_frame, image=self.image, text="      " + file, anchor=tk.NW, font=("Arial", 10), compound=tk.LEFT, highlightthickness=0, command=lambda: generate_tree_project_view(self, os.path.abspath(file)))
                self.open.image = self.image
                self.open.configure(background=PANEL_COLOR, foreground=FG_COLOR, bd=0)
                self.open.pack(side=tk.LEFT, padx=15, ipadx=5)
                self.open_frame.grid(row=row, sticky=tk.NW)

        generate_tree_project_view(self)

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True, ipadx=10)

    def refresh(self):
        generate_tree_project_view(self)


if __name__ == "__main__":
    generate_tree_project_view = None
    root = tk.Tk()
    Example(root, panel_width=60).pack(side="top", fill="both", expand=True)
    root.mainloop()
