import sys
import Screen
import Container
from shape import *
import pygame

#Set up the initial test shapes hard coded at the moment
Shapes = Container.Generate()

#Calculate the heat graph to be displayed in the GUI
heatMap = Container.calculateHeat(Shapes)

#Initialise the video window
pygame.init()

firstLaunch = True
done = False
clock = pygame.time.Clock()

while not done:
    #clock.tick(10)

    #Each refresh, fill the screen with White
    Screen.fillScreen(pygame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #INSERT EVENT HANDLER FOR WHEN NODES CHANGE GROUP/COLOURS

    Screen.drawShapes(pygame,Shapes)
    Screen.initDraw(pygame,heatMap)
    if firstLaunch:
        pygame.display.flip()
        bestContainer = Container.findContainer(pygame,Screen,heatMap)
        firstLaunch = False

    
    Screen.drawContainer(pygame,bestContainer)
    pygame.display.flip()

pygame.quit()

