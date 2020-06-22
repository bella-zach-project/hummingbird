import tkinter as tk

class vancas():
    def __init__(self, frame_width, frame_height, column, bar):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.column = column
        self.bar = bar
        self.master = tk.Tk()
        self.canvas = tk.Canvas(self.master,
                                width = self.frame_width,
                                height = self.frame_height)
        self.canvas.pack()
        self.column_sep = self.frame_width/self.column
        self.bar_sep = self.frame_height/self.bar
        self.first = True
        self.old_x = 0
        self.old_y = 0

    def graph(self, x, y):
        if self.first:
            self.old_x = x
            self.old_y = y
            print("i am first")
            self.first = False
        else:
            self.canvas.create_line(self.old_x, self.old_y, x, y)
            self.old_x = x
            self.old_y = y

    def draw_grid(self):
        csep1 = self.column_sep
        bsep1 = self.bar_sep
        for i in range(self.column):
            self.canvas.create_line(csep1, 0,csep1, self.frame_height)
            csep1 = csep1 + self.column_sep
        for i in range(self.bar):
            self.canvas.create_line(0, bsep1, self.frame_width, bsep1)
            bsep1 = bsep1 + self.bar_sep

