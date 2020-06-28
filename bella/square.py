import os, sys, math
import tkinter as tk
from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '..')))
from zach import canvas_project as zvc



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
	def draw(self, ox, oy):
		self.p.draw(ox, oy)
	def button_1(self, event):
		print ("clocled", event.x, event.y)
		self.draw(event.x, event.y)
cv = zvc.vancas(640, 640, 8, 8)
cv.draw_grid()
pic = picture()
cv.bind(pic)
pic.draw(300, 200)
pic.draw(100, 600)
input("type anything to stop");
