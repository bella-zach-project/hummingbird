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

def circ(s,x,y):
	global cv
	cv.new_graph()
	for i in range(200 + 1):
		a1 = i * ((2 *(math.pi)) / 200)
		x1 = s * (math.cos(a1)) + x
		y1 = s * (math.sin(a1)) + y
		cv.graph(x1,y1)	
circ(100, 500, 200)
input("type anything to stop");
