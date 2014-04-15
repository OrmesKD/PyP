import sys,calculator,optimiseContainer
from Object import *

class Handler:

	def __init__(self,shape_list):
		self.Shapes = shape_list

	def Search(self):
		Shapes = self.Shapes

		self.heatMap = calculator.calculateHeat(Shapes)

		bestContainer = calculator.findContainer(self.heatMap)

		return bestContainer

	def Move(self,container):
		oldContainer = container
		Shapes = self.Shapes
		heatMap = self.heatMap
		directions = ['LEFT','RIGHT','UP','DOWN']
		oppositeDirections = ['RIGHT','LEFT','DOWN','UP']
		moved = False

		for shape in Shapes:
			x1 = shape.getX1()
			x2 = shape.getX2()
			y1 = shape.getY1()
			y2 = shape.getY2()
#start of while loop here?
			while moved:
				for direction,oppositeDirection in zip(directions,oppositeDirections):

					shape.move(direction)
					new_heatMap = calculator.calculateHeat(Shapes)
					newContainer = calculator.findContainer(new_heatMap)

					if newContainer.getScore() > oldContainer.getScore():
						bestContainer = newContainer
						oldContainer = newContainer
						moved = True
						#update Screen
					else:
						shape.move(oppositeDirection)


