import sys
from numpy import *

class Node:

	def __init__(self,x,y,heat):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getHeat(self):
		return self.heat
			
