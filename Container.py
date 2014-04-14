import sys

class Container:

	def __init__(self,x1,y1,x2,y2,score):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.score = score

	def getX1(self):
        return self.x1
    def getX2(self):
        return self.x2
    def getY1(self):
        return self.y1
    def getY2(self):
        return self.y2