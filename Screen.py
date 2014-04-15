import sys,pygame,numpy,Node
from Object import *

# Colors that will be used in RGB format
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

size = [800,800]
rate = 8
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
	        screen.blit(text, (x*rate,y*rate))
	        y+=1
	    x+=1
	    y=0
	

def drawContainer(pygame,container):
	pygame.draw.rect(screen, RED, [container.getX1()*rate,container.getY1()*rate,(container.getX2()-container.getX1()+1)*rate,(container.getY2()-container.getY1()+1)*rate],1)
	

def drawShapes(pygame,Shapes):
	for shape in Shapes:
	    pygame.draw.rect(screen, BLACK, [shape.getX1()*rate,shape.getY1()*rate,(shape.getX2()-shape.getX1())*rate,(shape.getY2()-shape.getY1())*rate])
	

def drawText(pygame,heatMap):
	font = pygame.font.Font(None, 12)
	x = 0
	y = 0
	for row in heatMap:
		for e in row:
			if e < 51 or e > 99:
				text = font.render(str(e), True, (0,0,0))
				screen.blit(text, (x*rate,y*rate))
			y+=1
		x+=1
		y=0

def drawNodes(pygame,nodeList):
	font = pygame.font.Font(None, 12)
	for node in nodeList:
		text = font.render(str(node.getHeat()), True, node.getColour())
		screen.blit(text, (node.getX()*rate,node.getY()*rate))
	pygame.display.update()


