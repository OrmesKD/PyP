import sys
import Screen
import Container
from shape import *

#Set up the initial test shapes hard coded at the moment
Shapes = Container.Generate()

#Calculate the heat graph to be displayed in the GUI
Container.Calculate(Shapes)

#Draw the screen with the calculations found from the Container problem
Screen.draw(Shapes)