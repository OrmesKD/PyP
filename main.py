import sys
import pygame
from shape import *
from numpy import *

pygame.init()

# Colors that will be used in RGB format
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

size = [1000,1000]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Container example")

# Define the shapes
shape1 = Shape(20,20,30,60)
shape2 = Shape(60,20,80,40)
shape3 = Shape(20,60,80,70)
Shapes = [shape1,shape2,shape3]

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

# #Grouping points
# x = 0
# y = 0
# for row in heatMap:
#     for e in row:
#         if e = 0:
#             continue
#         #LEFT
#         if heatMap[x-1,y] > e-10 and heatMap[x-1,y] < e+10:
            
            

        


font = pygame.font.Font(None, 12)

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

    
    x = 0
    y = 0
    for row in heatMap:
        for e in row:
            text = font.render(str(e), True, (0,0,0))
            screen.blit(text, (x*10,y*10))
            y+=1
        x+=1
        y=0

    
                
        
    #Update display
    pygame.display.flip()

pygame.quit()
