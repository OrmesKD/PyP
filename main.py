import sys,Screen,Handler,pygame,cProfile
from Object import *

#MAIN FUNCTION TO PYPS
######################


#HARD CODED SHAPES, WILL REQUIRE BUTTON PRESS LATER.
shape1 = Shape(30,30,40,70)
shape2 = Shape(70,30,90,50)
shape3 = Shape(30,70,90,80)
Shapes = [shape1,shape2,shape3]
shapeGroups = []
shapeGroups.append([shape1,shape3])
shapeGroups.append([shape2])
#Intialise the handler object for the container methods
handler = Handler.Handler(Shapes)

#Initialise the video window
pygame.init()


firstLaunch = True
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(30)

    #Each refresh, fill the screen with White
    Screen.fillScreen(pygame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    Screen.drawShapes(pygame,Shapes)
    #Screen.initDraw(pygame,heatMap)
    if firstLaunch:
        pygame.display.flip()
        cProfile.run('bestContainer = handler.Search()')
        Screen.drawContainer(pygame,bestContainer)
        firstLaunch = False

    
    #Screen.drawContainer(pygame,bestContainer)
    handler.Move(bestContainer,shapeGroups,pygame)

pygame.quit()



