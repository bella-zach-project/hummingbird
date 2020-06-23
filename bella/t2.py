import os, sys
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from zach import t1 as zvc

cv = zvc.vancas(640, 640, 8, 8)
cv.draw_grid()

def sq(s,x,y):
	global cv
	# cv.new_graph()
	cv.graph(x - (s / 2.0), y - (s / 2.0))
	cv.graph(x + (s / 2.0), y - (s / 2.0))
	cv.graph(x + (s / 2.0), y + (s / 2.0))
	cv.graph(x - (s / 2.0), y + (s / 2.0))
	cv.graph(x - (s / 2.0), y - (s / 2.0))


sq(20, 155, 90)
sq(39, 500, 600)

input("type anything to stop");
