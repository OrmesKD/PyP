import sys
from numpy import *

class Node:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getNeighbours(heatMap,objMap):
		x = self.x
		y = self.y
		group = []
		#LEFT
		if x<0:
			
