import sys
import pygame
from Object import *
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
	for index,heat in ndenumerate(heatMap):
		if heat < 51:
			heatMap[index[0],index[1]] = 0

	# for row in heatMap:
	#     for e in row:
	#         if e < 51:
	#             heatMap[x,y] = 0
	#         y+=1
	#     x+=1
	#     y=0

	return heatMap

def search(Node,neighbourNode,Groups):
	n = Node
	heat = n.getHeat()
	neighbourHeat = neighbourNode.getHeat()

	groupFound = False
	if neighbourHeat >= heat-10 and neighbourHeat <= heat+10:
		if len(Groups) == 0:
			Groups.append([n,neighbourNode])
			print "Possible containers: " + str(len(Groups))
		else:
			for g in Groups:
				if neighbourNode.belongsTo(g) == True:
					if n.belongsTo(g):
						break
					else:
						g.append(n)
						break
				elif n.belongsTo(g) == True:
					if neighbourNode.belongsTo(g):
						break
					else:
						g.append(neighbourNode)
						break
			else:
				Groups.append([n,neighbourNode])
				print "Possible containers: " + str(len(Groups))
	return Groups

def findContainer(heatMap):
	nodeList = array(Node)
	
	#Generate Nodes from Points on heatMap
	x = 0
	y = 0
	for index,heat in ndenumerate(heatMap):
		if heat > 50:
			nodeList.append(Node(index[0],index[1],heat))

	# for row in heatMap:
	#     for heat in row:
	#         if heat < 50:
	#         	y+=1
	#         	continue
	#         else:
	#         	nodeList.append(Node(x,y,heat))
	#         y+=1 
	#     x+=1
	#     y=0
	
	#Group nodes in to possible container areas
	Groups = []
	
	for n in nodeList:
		x = n.getX()
		y = n.getY()
		
		#LEFT
		if nodeExists(nodeList,n,x-1,y) == True:
			neighbourNode = findNode(nodeList,n,x-1,y)
			Groups = search(n,neighbourNode,Groups)
			
						
		#RIGHT
		if nodeExists(nodeList,n,x+1,y) == True:
			neighbourNode = findNode(nodeList,n,x+1,y)
			Groups = search(n,neighbourNode,Groups)

		#UP
		if nodeExists(nodeList,n,x,y-1) == True:
			neighbourNode = findNode(nodeList,n,x,y-1)
			Groups = search(n,neighbourNode,Groups)

		
		#DOWN
		if nodeExists(nodeList,n,x,y+1) == True:
			neighbourNode = findNode(nodeList,n,x,y+1)
			Groups = search(n,neighbourNode,Groups)

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
		if node.getX() >= highestX and node.getY() >= highestY:
			highestX = node.getX()
			highestY = node.getY()

	print "Number of groups: " + str(len(Groups))
	print "Score of group: " + str(bestScore)
	print "Lowest: " + str(lowestX) + ", " + str(lowestY)
	print "Highest: " + str(highestX) + ", " + str(highestY)

	bestContainer = Container(lowestX,lowestY,highestX,highestY)
	bestContainer.setScore(bestScore)

	return bestContainer

	






