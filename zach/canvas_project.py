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
        self.scale_x = (self.frame_width/2000.0)
        self.off_x = (self.frame_width/2)
        self.scale_y = (-self.frame_height/2000.0)
        self.off_y = (self.frame_height/2)
        self.rscale_x = (1/self.scale_x)
        self.rscale_y = (1/self.scale_y)

    def mainloop(self):
        self.master.mainloop()

    def bind(self, pic):
        self.pic = pic
        self.canvas.bind("<Button-1>", self.button_1)
        
    def button_1(self, event):
        event.x = (event.x-self.off_x)*(self.rscale_x)
        event.y = (event.y-self.off_y)*(self.rscale_y)
        self.pic.button_1(event)

    def graph(self, x, y):
        if self.first:
            self.old_x = x
            self.old_y = y
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

    def new_graph(self):
        self.first = True
    
    def vert(self, x, y):
        new_x = self.scale_x*x + self.off_x
        new_y = self.scale_y*y + self.off_y
        self.graph(new_x, new_y)

    def clear_screen(self):
        self.canvas.delete(all)

class picture():
    def __init__(self, obj):
        self.obj = obj

    def draw(self, ox, oy):
        self.obj.new_graph()
        self.obj.vert(ox-10, oy-10)
        self.obj.vert(ox+10, oy+10)
        self.obj.new_graph()
        self.obj.vert(ox+10, oy-10)
        self.obj.vert(ox-10, oy+10)

    def button_1(self, event):
        self.draw(event.x, event.y)


def main():
        obj = vancas(600, 600, 10, 10)
        obj.new_graph()
        pic = picture(obj)
        pic.draw(50, 50)
        obj.bind(pic)
        obj.mainloop()
        
if __name__ == "__main__":
        main()
