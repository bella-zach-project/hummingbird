import os, sys, math
import tkinter as tk
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from zach import canvas_project as zvc

def debug(ox, oy, x, y, s):
	global cv
#	cv.new_graph()
#	cv.vert(x, y)
#	cv.vert(ox, oy)
	cv.new_graph()
	for i in range(17):
		a1 = i * ((2 *(math.pi)) / 16)
		x1 = s * (math.cos(a1)) + ox
		y1 = s * (math.sin(a1)) + oy
		cv.vert(x1,y1)	


class epi():
	def __init__(self, s, sa, rate, p = None):
		self.s = s
		self.sa = sa
		self.p = p
		self.rate = rate
	def draw(self, ox, oy, t):
		global cv
		a1 = (t * self.rate) + self.sa
		x1 = self.s * (math.cos(a1)) + ox
		y1 = self.s * (math.sin(a1)) + oy
		debug(ox, oy, x1, y1, self.s)
		if self.p:
			self.p.draw(x1, y1, t)
		else:
			cv.new_graph()
			cv.vert(x1 + 10,y1 - 10)	
			cv.vert(x1 - 10,y1 + 10)	
			cv.new_graph()
			cv.vert(x1 - 10,y1 - 10)	
			cv.vert(x1 + 10,y1 + 10)	

class poly():
	def __init__(self, s, a, p = None):
		self.s = s
		self.a = a
		self.p = p
		if p:
			self.count = a
		else:
			self.count = a + 1
	def draw(self, ox, oy, r = 0):
		global cv
		cv.new_graph()
		for i in range(self.count):
			a1 = i * ((2 *(math.pi)) / self.a) + r
			x1 = self.s * (math.cos(a1)) + ox
			y1 = self.s * (math.sin(a1)) + oy
			if self.p:
				self.p.draw(x1, y1, r = a1)
			else:
				cv.vert(x1,y1)	

class picture():
	def __init__(self):
		self.q = poly(100, 45)
		self.p = poly(100,12, self.q)
		self.e1 = epi(100,         0, -1)
		self.e0 = epi(100, math.pi/4,  1, self.e1)
		self.t = 0
	def draw_epi(self):
		self.e0.draw(0, 0, self.t)
		self.t = self.t + 1
	def draw(self, ox, oy):
		self.p.draw(ox, oy)
	def button_1(self, event):
		self.draw_epi()
cv = zvc.vancas(640, 640, 8, 8)
cv.draw_grid()
pic = picture()
cv.bind(pic)
pic.draw_epi()
pic.draw(300, 200)
pic.draw(100, 600)

input("type anything to stop");
