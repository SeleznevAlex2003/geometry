from tkinter import Tk, Canvas, Frame, BOTH
class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("geometry")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        self.draw_triangle(canvas, 55, 85, 155, 85, 105, 180, "red")
        self.draw_square(canvas, 10, 10, 80, "blue")
        self.draw_romb(canvas, 200, 200, 350, 200, 400, 400, 250, 400, "green")
        canvas.pack(fill=BOTH, expand=1)

    def draw_triangle(self, master, x1, y1, x2, y2, x3, y3, color):
        # made by ILIA
        master.create_polygon([x1, y1, x2, y2, x3, y3], outline=color, fill=color, width=2)

    def draw_square(self, master, x, y, side_size, color):
        #made by ALEX
        master.create_polygon([x, y, x + side_size, y, x + side_size, y + side_size, x, y + side_size],
                              outline=color, fill=color, width=2)

    def draw_romb(self, master, x1, y1, x2, y2, x3, y3, x4, y4, color):
        #made by ALEX
        master.create_polygon([x1, y1, x2, y2, x3, y3, x4, y4], outline=color, fill=color, width=2)

def main():
    root = Tk()
    ex = Example()
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
