
import tkinter
from tkinter import ttk

from Model.account import Account

class KTable(ttk.Frame):

    def __init__(self, parent, headers, data, currentData, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.rows = []
        self.currentData = currentData
        self.headers = headers
        self.data = data
        self.draw()
        #self.configureRowInteractivity()

    def drawHeader(self):
        self.headerCanvas = tkinter.Canvas(
            self,
            height=self['height'] * 0.1,
            width=self['width'] * 0.97,
            background="#e3e3e3",
            bd=0,
            highlightthickness=0
        )
        self.headerCanvas.bind("<Button-1>", lambda x: print("click"))

        for idx, val in enumerate(self.headers):
            self.headerCanvas.create_text(
                self['width'] - ((self['width'] // 6) * (5-idx)),
                self['height'] *0.1 * 0.5,
                text=val,
                fill="black",
            )

        #self.headerCanvas.grid(column=0, row=0, sticky=tkinter.EW)
        self.headerCanvas.pack()
    
    def setCurrentData(self, event, row, widget : tkinter.Canvas):
        self.currentData = Account(list(row))
        widget.configure(background='#b8ecff')

        for idx, canvas in enumerate(self.rows):
            if canvas == widget:
                continue
            canvas.configure(background="white" if idx % 2 == 0 else "#f0f0f0")

    def drawData(self):
        for idx, row in enumerate(self.data):
            dataCanvas = tkinter.Canvas(
                self,
                height=self['height'] * 0.1,
                width=self['width'] * 0.97,
                background="white" if idx % 2 == 0 else "#f0f0f0",
                bd=0,
                highlightthickness=0
            )

            dataCanvas.bind('<Button-1>', lambda event, row=row, widget=dataCanvas : self.setCurrentData(event, row, widget))

            for jdx, val in enumerate(row):
                dataCanvas.create_text(
                    self['width'] - ((self['width'] // 6) * (5-jdx)),
                    self['height'] *0.1 * 0.5,
                    text=val,
                    fill="black",
                )

            #dataCanvas.grid(column=0, row=idx+1, sticky=tkinter.EW)
            self.rows.append(dataCanvas)
            dataCanvas.pack()

    def draw(self):
        self.drawHeader()
        self.drawData()

