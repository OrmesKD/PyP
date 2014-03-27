import sys
from shape import *
from numpy import *
from Node import *

def Generate():
	# Define the shapes
	shape1 = Shape(20,20,30,60)
	shape2 = Shape(60,20,80,40)
	shape3 = Shape(20,60,80,70)
	Shapes = [shape1,shape2,shape3]

	return Shapes

def calculateHeat(Shapes):
	

	heatMap = zeros((100,100), dtype=int)
	objMap = zeros((100,100), dtype=int)
	posPoints = zeros((100,100),dtype=int)

	for shape in Shapes:
	    xx=shape.getX1()
	    yy=shape.getY1()
	    while yy < shape.getY2():
	        if xx == shape.getX2():
	            xx=shape.getX1()
	            yy+=1
	        if yy > shape.getY2()-1:
	            continue
	        objMap[xx,yy] = 1
	        xx+=1

	for shape in Shapes:
	    heatMap = shape.edges(heatMap,objMap)

	#Rules out all areas that are not considered for containers
	x = 0
	y = 0
	for row in heatMap:
	    for e in row:
	        if e < 51 or e > 99:
	            heatMap[x,y] = 0
	        y+=1
	    x+=1
	    y=0

	return heatMap

def findContainer(heatMap):
	nodeList = []
	
	#Generate Nodes from Points on heatMap
	x = 0
	y = 0
	for row in heatMap:
	    for heat in row:
	        if heat == 0:
	            continue
	        else:	
	        	nodeList.append(Node(x,y,heat))
	        x+=1
	    y+=1
	
	#Group nodes in to possible container areas
	Groups = []
	for n in nodeList:
		x = n.getX()
		y = n.getY()
		heat = n.getHeat()
		groupFound = False
		#LEFT
		if x > 0:
			if heatMap[x-1,y] > heat-10 and heatMap[x-1,y] < heat+10:
				for neighbour in nodeList:
					if neighbour.getX() == x-1 and neighbour.getY() == y:
						neighbourNode = neighbour
						break
					else:
						continue
				for g in Groups:
					if neighbourNode.belongsTo(g):
						g.append(n)
					else:
						continue
				if groupFound == False:
					Groups.append([n,neighbourNode])



