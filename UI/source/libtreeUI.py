# ************************
# Scrollable Frame Class
# ************************

import os
import sys
import glob
import tkinter as tk

import libcom

from cfg import GEOMETERY, BG_COLOR, FG_COLOR, PANEL_COLOR, STATUS_COLOR, \
    BORDER_COLOR, TOOL_COLOR, SIDETOOL_COLOR, PEN_COLOR, ADD, CARD, CLOUD, \
    FILE, GRAPH, MONEY, REFRESH, SAVE, SETTINGS, RESOURCE_PATH, COMPONENT_PATH


# Function definition
def generate_tree_project_view(self):
    pass


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


class ScrollFrameHorizontal(tk.Frame):
    def __init__(self, parent, *args, **kw):
        super().__init__(parent, *args, **kw)
        self.panel_width = None

    def construct(self):
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, width=self.panel_width, height=35)
        self.canvas.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=1)
        self.viewPort = tk.Frame(self.canvas, highlightthickness=0, width=self.panel_width, height=35)
        self.vsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview, background=PANEL_COLOR)
        self.canvas.configure(xscrollcommand=self.vsb.set)

        self.vsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="x", expand=True)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.viewPort, anchor="nw", tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

        self.onFrameConfigure(None)

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_height = event.height
        self.canvas.itemconfig(self.canvas_window, height=canvas_height)


class PanelTree(tk.Frame):
    def __init__(self, root, panel_width):
        tk.Frame.__init__(self, root)
        global generate_tree_project_view, PATH
        self.scrollFrame = ScrollFrame(self)
        self.scrollFrame.panel_width = panel_width
        self.scrollFrame.construct()
        self.scrollFrame.viewPort.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=0)
        PATH = os.getcwd()

        def generate_tree_project_view(self, dir=os.getcwd()+'/'):
            global PATH, self_pointer
            self_pointer = self

            row = 0
            # clean previous list
            for child in self.scrollFrame.viewPort.winfo_children():
                child.destroy()
            print("DIR", dir)
            # the heading of the project panel
            tk.Label(self.scrollFrame.viewPort, background=PANEL_COLOR).grid(row=row)
            PATH = os.path.abspath(dir).split('\\' if sys.platform == 'win32' else '/')[-2]
            # load the current project working directory
            for file in [PATH] + glob.glob(dir + '*'):
                row += 1
                if os.path.isdir(file):
                    self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/open.png').subsample(2, 2)
                else:
                    self.image = tk.PhotoImage(file=os.getcwd() + '/resource/tool/file.png').subsample(2, 2)
                # NOTE: the child controls are added to the view port (scrollFrame.viewPort, NOT scrollframe itself)
                self.open_frame = tk.Frame(self.scrollFrame.viewPort)
                self.open_frame.configure(background=PANEL_COLOR)

                def theme_button_tree(put=file):
                    global generate_tree_project_view, self_pointer
                    ui = tk.Button(self.open_frame, image=self.image, text="      " + os.path.basename(file), anchor=tk.NW, font=("Arial", 10), compound=tk.LEFT, highlightthickness=0)

                    def do():
                        global generate_tree_project_view, self_pointer
                        selection = ui.cget('text').replace(' ', '')
                        libcom.CurrentTab.value = selection
                        p = ui.cget('text').replace(' ', '')
                        if os.path.abspath(p).split('\\' if sys.platform == 'win32' else '/')[-1] == os.path.abspath(p).split('\\' if sys.platform == 'win32' else '/')[-2]:
                            exec("generate_tree_project_view(self_pointer, '" + '/'.join(os.path.abspath(p).split('\\' if sys.platform == 'win32' else '/')[:-1]) + "/')")
                        else:
                            exec("generate_tree_project_view(self_pointer, '" + '/'.join(os.path.abspath(p).split('\\' if sys.platform == 'win32' else '/')) + "/')")

                    ui.configure(command=do)
                    ui.image = self.image
                    ui.configure(background=PANEL_COLOR, foreground=FG_COLOR, bd=0)
                    ui.pack(side=tk.LEFT, padx=15, ipadx=5)
                    ui.bind("<Enter>", lambda x: ui.configure(background=TOOL_COLOR))
                    ui.bind("<Leave>", lambda x: ui.configure(background=PANEL_COLOR))

                theme_button_tree()

                self.open_frame.grid(row=row, sticky=tk.NW)

        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="top", fill="both", expand=True, ipadx=10)

    def refresh(self):
        generate_tree_project_view(self)


class TabTree(tk.Frame):
    def __init__(self, root, panel_width):
        tk.Frame.__init__(self, root)
        global generate_tree_project_view, PATH
        self.scrollFrame = ScrollFrameHorizontal(self)
        self.scrollFrame.panel_width = panel_width
        self.scrollFrame.construct()
        self.scrollFrame.viewPort.configure(background=PANEL_COLOR, highlightbackground=BORDER_COLOR, highlightcolor=BORDER_COLOR, highlightthickness=0)
        # when packing the scrollframe, we pack scrollFrame itself (NOT the viewPort)
        self.scrollFrame.pack(side="bottom", fill="x", expand=True, ipadx=10)

    def refresh(self):
        generate_tree_project_view(self)


def test():
    root = tk.Tk()
    panel = PanelTree(root, panel_width=60)
    panel.refresh()
    panel.pack(side="top", fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    test()
