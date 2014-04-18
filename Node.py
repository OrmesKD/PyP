import sys
from numpy import *

class Node:

	def __init__(self,x,y,heat):
		self.x = x
		self.y = y
		self.heat = heat
		self.colour = (0,0,0)
		self.group = 0

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getHeat(self):
		return self.heat

	def getColour(self):
		return self.colour

	def setColour(self,newColour):
		self.colour = newColour

	def setGroup(self,group):
		self.group = group

	def belongsTo(self,group):
		if self.group == group:
			return True
		return False
			
