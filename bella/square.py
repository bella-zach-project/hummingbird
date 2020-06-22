import canvas_project as zvc

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
