import sys,calculator,Screen
from Object import *

class Handler:

	def __init__(self,shape_list):
		self.Shapes = shape_list

	def Search(self):
		Shapes = self.Shapes

		self.heatMap = calculator.calculateHeat(Shapes)

		bestContainer = calculator.findContainer(self.heatMap)

		return bestContainer

	def update(self,pygame,Shapes,heatMap,Container):
		Screen.fillScreen(pygame)
		Screen.drawShapes(pygame,Shapes)
		Screen.drawContainer(pygame,Container)

	def Move(self,container,shapeGroups,pygame):
		oldContainer = container
		Shapes = self.Shapes
		heatMap = self.heatMap
		
		moved = True

		for shapeg in shapeGroups:
			directions = ['LEFT','RIGHT','UP','DOWN']
			oppositeDirections = ['RIGHT','LEFT','DOWN','UP']
			while moved:
				count=0
				for direction,oppositeDirection in zip(directions,oppositeDirections):
					print 'Trying '+direction
					for shape in shapeg:
						print 'Shape: ' + str(shape.getX1())+ ' '+ str(shape.getY1())
						shape.move(direction)
					new_heatMap = calculator.calculateHeat(Shapes)
					newContainer = calculator.findContainer(new_heatMap)

					if newContainer.getScore() > oldContainer.getScore():
						print "Better container found!"
						bestContainer = newContainer
						oldContainer = newContainer
						heatMap = new_heatMap
						count+=1
						#for shape in shapeg:
						#	shape.removeDirection(oppositeDirection)
						try:
							directions.remove(oppositeDirection)
							oppositeDirections.remove(direction)
						except ValueError:
							pass

						self.update(pygame,Shapes,heatMap,bestContainer)
						
					else:
						for shape in shapeg:
							shape.move(oppositeDirection)
					self.update(pygame,Shapes,heatMap,oldContainer)
				if count == 0:
					moved=False


