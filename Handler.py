import sys,Container,optimiseContainer
from shape import *

class Handler:

	def __init__(self,shape_list):
		self.Shapes = shape_list

	def Search(self):
		Shapes = self.Shapes

		heatMap = Container.calculateHeat(Shapes)

		bestContainer = Container.findContainer(heatMap)

		return bestContainer

	#def Move(self):





