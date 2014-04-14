import sys,calculator,optimiseContainer
from shape import *

class Handler:

	def __init__(self,shape_list):
		self.Shapes = shape_list

	def Search(self):
		Shapes = self.Shapes

		self.heatMap = calculator.calculateHeat(Shapes)

		bestContainer = calculator.findContainer(self.heatMap)

		return bestContainer

	def Move(self):
		Shapes = self.Shapes
		heatMap = self.heatMap

		for shape in Shapes:
			x1 = shape.getX1()
			x2 = shape.getX2()
			y1 = shape.getY1()
			y2 = shape.getY2()




		#Move left
			shape.move('LEFT')
			new_heatMap = calculator.calculateHeat(Shapes)
			newContainer = calculator.findContainer(new_heatMap)


		#Move right

		#Move up

		#Move down




