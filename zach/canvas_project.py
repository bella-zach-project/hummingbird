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
        self.canvas.bind("mouse-1", self.mouse_event)
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

    def new_graph(self):
        self.first = True
    
    def vert(self, x, y):
        new_x = self.scale_x*x + self.off_x
        new_y = self.scale_y*y + self.off_y
        self.graph(new_x, new_y)

    def mouse_event(self, event):
        print ("clicked", event.x, event.y)

def main():
        obj = vancas(600, 600, 10, 10)
#        obj.draw_grid()
        obj.new_graph()
        obj.graph(0, 0)
        obj.graph(4, 4)
        obj.new_graph()
        obj.vert(0, 0)
        obj.vert(900, 900)
        obj.vert(900, 0)
        obj.vert(0, 0)
        obj.master.mainloop()
        
if __name__ == "__main__":
        main()
