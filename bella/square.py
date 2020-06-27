import os, sys, math
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from zach import canvas_project as zvc

cv = zvc.vancas(640, 640, 8, 8)
cv.draw_grid()

def sq(s,x,y):
	global cv
	cv.new_graph()
	cv.graph(x - (s / 2.0), y - (s / 2.0))
	cv.graph(x + (s / 2.0), y - (s / 2.0))
	cv.graph(x + (s / 2.0), y + (s / 2.0))
	cv.graph(x - (s / 2.0), y + (s / 2.0))
	cv.graph(x - (s / 2.0), y - (s / 2.0))


sq(20, 155, 90)
sq(39, 500, 600)

def circ(s,cx, cy,x,y):
	global cv
	dx = x - cx
	dy = y - cy
	sq(10, x, y)
	cv.new_graph()
	a = (2 * math.pi) / s
	cos = math.cos(a)
	sin = math.sin(a)
	for _ in range(s + 1):
		cv.graph(dx + cx , dy + cy)
		newx = dx * cos - dy * sin
		newy = dx * sin + dy * cos
		dx = newx
		dy = newy

circ(100, 500, 200, 520, 3)


def poly(s,a,x,y):
	global cv
	cv.new_graph()
	for i in range(a + 1):
		a1 = i * ((2 *(math.pi)) / a)
		x1 = s * (math.cos(a1)) + x
		y1 = s * (math.sin(a1)) + y
		cv.graph(x1,y1)	
poly(300,5, 400, 350)

input("type anything to stop");
