import sys
from shape import *
from numpy import *
from Node import *

def Generate():
	# Define the shapes HARD CODED ATM, SHAPES SHOULD BE PASSED IN FINAL
	shape1 = Shape(20,20,30,60)
	shape2 = Shape(60,20,80,40)
	shape3 = Shape(20,60,80,70)
	Shapes = [shape1,shape2,shape3]

	return Shapes

def findNode(nodeList,targetNode,x,y):
	#Function used for finding a Node with the given x,y coordinates
	for n in nodeList:
		if n.getX() == x and n.getY() == y:
			return n

def nodeExists(nodeList,targetNode,x,y):
	for n in nodeList:
		if n.getX() == x and n.getY() == y:
			return True
		else:
			continue
		return False

def calculateHeat(Shapes):
	#Function for calculating considered heat points on the map

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
	        	x+=1
	        	continue
	        else:
	        	nodeList.append(Node(x,y,heat))
	        x+=1 
	    y+=1
	    x=0
	
	#Group nodes in to possible container areas
	Groups = []
	count = 1
	for n in nodeList:
		print count
		count+=1
		x = n.getX()
		y = n.getY()
		heat = n.getHeat()

		#print "Groups: " + str(len(Groups))
		#LEFT -- Being edited.
		if x > 0 and nodeExists(nodeList,n,x-1,y) == True:
			neighbourNode = findNode(nodeList,n,x-1,y)
			neighbourHeat = neighbourNode.getHeat()
			groupFound = False
			if neighbourHeat > heat-10 and neighbourHeat < heat+10:
				if len(Groups) == 0:
					Groups.append([n,neighbourNode])
				else:
					for g in Groups:
						if neighbourNode.belongsTo(g) == True:
							g.append(n)
							break
						elif n.belongsTo(g) == True:
							g.append(neighbourNode)
							break
					else:
						Groups.append([n,neighbourNode])
						
		
		#RIGHT
		if x < 100 and nodeExists(nodeList,n,x+1,y) == True:
			neighbourNode = findNode(nodeList,n,x+1,y)
			neighbourHeat = neighbourNode.getHeat()
			groupFound = False
			if neighbourHeat > heat-10 and neighbourHeat < heat+10:
				if len(Groups) == 0:
					Groups.append([n,neighbourNode])
				else:
					for g in Groups:
						if neighbourNode.belongsTo(g) == True:
							g.append(n)
							break
						elif n.belongsTo(g) == True:
							g.append(neighbourNode)
							break
					else:
						Groups.append([n,neighbourNode])
		
		#UP
		if y > 0 and nodeExists(nodeList,n,x,y-1) == True:
			neighbourNode = findNode(nodeList,n,x,y-1)
			neighbourHeat = neighbourNode.getHeat()
			groupFound = False
			if neighbourHeat > heat-10 and neighbourHeat < heat+10:
				if len(Groups) == 0:
					Groups.append([n,neighbourNode])
				else:
					for g in Groups:
						if neighbourNode.belongsTo(g) == True:
							g.append(n)
							break
						elif n.belongsTo(g) == True:
							g.append(neighbourNode)
							break
					else:
						Groups.append([n,neighbourNode])
		
		#DOWN
		if y < 100 and nodeExists(nodeList,n,x,y+1) == True:
			neighbourNode = findNode(nodeList,n,x,y+1)
			neighbourHeat = neighbourNode.getHeat()
			groupFound = False
			if neighbourHeat > heat-10 and neighbourHeat < heat+10:
				if len(Groups) == 0:
					Groups.append([n,neighbourNode])
				else:
					for g in Groups:
						if neighbourNode.belongsTo(g) == True:
							g.append(n)
							break
						elif n.belongsTo(g) == True:
							g.append(neighbourNode)
							break
					else:
						Groups.append([n,neighbourNode])
	bestScore = 0
	bestGroup = []
	for g in Groups:
		score = 0
		for node in g:
			score += node.getHeat()
		if score > bestScore:
			bestScore = score
			bestGroup = g

	lowestX = 100
	lowestY = 100
	highestX = 0
	highestY = 0
	for node in bestGroup:
		if node.getX() < lowestX and node.getY() < lowestY:
			lowestX = node.getX()
			lowestY = node.getY()
	for node in bestGroup:
		if node.getX() > highestX and node.getY() > highestY:
			highestX = node.getX()
			highestY = node.getY()

	print "Number of groups: " + str(len(Groups))
	print "Lowest: " + str(lowestX) + ", " + str(lowestY)
	print "Highest: " + str(highestX) + ", " + str(highestY)

	






