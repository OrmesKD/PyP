import sys,Screen,Handler,pygame
from shape import *

#MAIN FUNCTION TO PYPS
######################


#HARD CODED SHAPES, WILL REQUIRE BUTTON PRESS LATER.
shape1 = Shape(20,20,30,60)
shape2 = Shape(60,20,80,40)
shape3 = Shape(20,60,80,70)
Shapes = [shape1,shape2,shape3]

#Intialise the handler object for the container methods
handler = Handler.Handler(Shapes)

#Initialise the video window
pygame.init()


firstLaunch = True
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    #Each refresh, fill the screen with White
    Screen.fillScreen(pygame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    Screen.drawShapes(pygame,Shapes)
    #Screen.initDraw(pygame,heatMap)
    if firstLaunch:
        pygame.display.flip()
        bestContainer = handler.Search()
        firstLaunch = False

    
    Screen.drawContainer(pygame,bestContainer)
    pygame.display.flip()

pygame.quit()

