import sys, pygame
from numpy import *

class Shape:

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        

    def getX1(self):
        return self.x1
    def getX2(self):
        return self.x2
    def getY1(self):
        return self.y1
    def getY2(self):
        return self.y2
    

    def setX1(x):
        self.x1 = x
    def setX2(x):
        self.x2 = x
    def setY1(y):
        self.y1 = y
    def setY2(y):
        self.y2 = y

    def edges(self,common,objectMap):
        self.common = common.copy()
        
        x1=self.x1
        y1=self.y1
        x2=self.x2
        y2=self.y2

        #TopLeft to TopRight Edge
        xx=x1
        yy=y1-1
        heat=50
        while xx<x2:
            if yy == y1-50 or yy==0 or objectMap[xx,yy]==1:
                heat=50
                yy=y1
                xx+=1
            common[xx,yy] += heat
            
            heat-=1
            yy=yy-1

        #TopRight to BottomRight Edge
        xx=x2+1
        yy=y1
        heat=50
        while yy<y2:
            if xx == x2+50 or xx ==100 or objectMap[xx,yy]==1:
                heat=50
                xx=x2
                yy+=1
            common[xx,yy] += heat
            heat-=1
            xx=xx+1

        #BottomLeft to BottomRight Edge
        xx=x1
        yy=y2+1
        heat=50
        while xx<x2:
            if yy == y2+50 or yy==100 or objectMap[xx,yy]==1:
                heat=50
                yy=y2
                xx+=1
            common[xx,yy] += heat
            heat-=1
            yy=yy+1

        #TopLeft Edge to BottomLeft Edge
        xx=x1-1
        yy=y1
        heat=50
        while yy<y2:
            if xx == x1-50 or xx==0 or objectMap[xx,yy]==1:
                heat=50
                xx=x1
                yy+=1
            common[xx,yy] += heat
            heat-=1
            xx=xx-1
        
        

        return common
