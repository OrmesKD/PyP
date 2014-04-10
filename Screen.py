import sys
import pygame
import shape
import numpy
import Node

# Colors that will be used in RGB format
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

size = [1000,1000]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Container example")

def fillScreen(pygame):
	screen.fill(WHITE)

def initDraw(pygame,heatMap):
	font = pygame.font.Font(None, 12)
	x = 0
	y = 0
	for row in heatMap:
	    for e in row:
	        text = font.render(str(e), True, (0,0,0))
	        screen.blit(text, (x*10,y*10))
	        y+=1
	    x+=1
	    y=0
	pygame.display.flip()

def drawContainer(pygame,container):
	pygame.draw.rect(screen, RED, [container[1]*10,container[0]*10,container[3]*10,container[2]*10],1)

def drawShapes(pygame,Shapes):
	for shape in Shapes:
	    pygame.draw.rect(screen, BLACK, [shape.getX1()*10,shape.getY1()*10,(shape.getX2()-shape.getX1())*10,(shape.getY2()-shape.getY1())*10])
	pygame.display.flip()

def drawText(pygame,heatMap):
	font = pygame.font.Font(None, 12)
	x = 0
	y = 0
	for row in heatMap:
		for e in row:
			if e < 51 or e > 99:
				text = font.render(str(e), True, (0,0,0))
				screen.blit(text, (x*10,y*10))
			y+=1
		x+=1
		y=0

def drawNodes(pygame,nodeList):
	font = pygame.font.Font(None, 12)
	for node in nodeList:
		text = font.render(str(node.getHeat()), True, node.getColour())
		screen.blit(text, (node.getX()*10,node.getY()*10))
	pygame.display.update()


