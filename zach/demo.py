#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=3000)
        self.grid()
        self.createWidgets('Hello there',0)
        self.createWidgets('Bye',1)

    def createWidgets(self, t, c):
        self.quitButton = tk.Button(self, text=t,
            command=self.quit)
        self.quitButton.grid(column=c, row = 0)

app = Application()
app.master.title('Sample application')
app.mainloop()                     
print('hello there')
