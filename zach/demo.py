#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=3000)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.canvasFrame = tk.canvas(self, command=self.quit)
        self.canvasFrame.grid(column=0, row = 0)


app = Application()
app.master.title('Draw')
app.mainloop()                     
