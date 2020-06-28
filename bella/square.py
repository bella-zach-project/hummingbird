import os, sys, math
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from zach import canvas_project as zvc

cv = zvc.vancas(640, 640, 8, 8)
cv.draw_grid()

def sq(s,x,y):
	global cv
	cv.new_graph()
	cv.vert(x - (s / 2.0), y - (s / 2.0))
	cv.vert(x + (s / 2.0), y - (s / 2.0))
	cv.vert(x + (s / 2.0), y + (s / 2.0))
	cv.vert(x - (s / 2.0), y + (s / 2.0))
	cv.vert(x - (s / 2.0), y - (s / 2.0))


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
		cv.vert(dx + cx , dy + cy)
		newx = dx * cos - dy * sin
		newy = dx * sin + dy * cos
		dx = newx
		dy = newy

circ(100, 500, 200, 520, 3)


class poly():
	def __init__(self, s, a, p = None):
		self.s = s
		self.a = a
		self.p = p
		if p:
			self.count = a
		else:
			self.count = a + 1
	def draw(self, ox, oy):
		global cv
		cv.new_graph()
		for i in range(self.count):
			a1 = i * ((2 *(math.pi)) / self.a)
			x1 = self.s * (math.cos(a1)) + ox
			y1 = self.s * (math.sin(a1)) + oy
			if self.p:
				self.p.draw(x1, y1)
			else:
				cv.vert(x1,y1)	
q = poly(100, 20)
p = poly(100,12, q)
p.draw(400, 500)
input("type anything to stop");
