from turtle import Turtle
class Ball(Turtle):
	def __init__(self, radius, color, dx, dy):
		Turtle.__init__(self)
		self.circle(radius)
		self.color(color)
		self.dx=dx
		self.dy=dy
	def move_x(self,num):
		dx=num*(self.dx+1)
	def move_y(self, steps):
		dy=num*(self.dy+1)
turtle=Ball(10, 'purple', 20, 21)
turtle.penup()
turtle.shape('circle')




