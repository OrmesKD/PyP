import sys
import pygame
import shape
import numpy

# Colors that will be used in RGB format
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

size = [1000,1000]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Container example")

def renderText(heatMap):
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

def draw(Shapes,heatMap):
	pygame.init()

	#Loop until the user clicks the close button
	done = False
	clock = pygame.time.Clock()

	while not done:
	    clock.tick(10)

	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            done=True

	    screen.fill(WHITE)

	    for shape in Shapes:
	        pygame.draw.rect(screen, BLACK, [shape.getX1()*10,shape.getY1()*10,(shape.getX2()-shape.getX1())*10,(shape.getY2()-shape.getY1())*10])

	    
	    renderText(heatMap)

	    
	                
	        
	    #Update display
	    pygame.display.flip()

	pygame.quit()
