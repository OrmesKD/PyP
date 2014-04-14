import pygame
pygame.init()

# handle pygame basic window
# handle event loop
class Window:
   def __init__(self,caption,size,flags=0,depth=0,fps=30):
      self.fps = fps # frames per second
      
      self.screen = pygame.display.set_mode(size,flags,depth)
      pygame.display.set_caption(caption)

      self.clock = pygame.time.Clock() # use to control framerate
      self.Window_Open = True
      self.Run = True
      
      self.updatefunc = None
      self.eventfunc = None
      
   def SetPage(self,updatefunc = None,eventfunc = None):
      self.updatefunc = updatefunc
      self.eventfunc = eventfunc
      
   def Flip(self):
      self.Run = True
      while self.Run and self.Window_Open:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.Window_Open = False
            else:
               if self.eventfunc is not None:
                  self.eventfunc(event)

         if self.updatefunc is not None:
            self.updatefunc(self.screen)
               
         pygame.display.flip()
         self.clock.tick(self.fps)

# hilight clickable box.         
class Button:
   def __init__(self,text,pos,size=(100,30),color=(0,0,200),hilight=(0,200,200)):
      self.normal = color
      self.hilight = hilight
      self.rect = pygame.Rect(pos,size)
      self.mouseover = False
      self.text = text
      self.font = pygame.font.Font(None,24)
      self.text_image = self.font.render(text,1,(255,255,255))
      w,h = self.font.size(text) # size of font image
      self.text_pos = (pos[0] + size[0] / 2 - w / 2,pos[1] + size[1] / 2 - h / 2) # center text
      self.buttondown = False
      
   def Draw(self,surface):
      rectout = self.rect.inflate(2,2)
      rectin = self.rect.inflate(1,1)
      if self.buttondown:
         pygame.draw.rect(surface,(0,0,0),rectout)
         pygame.draw.rect(surface,(255,255,255),rectin)
      else:
         pygame.draw.rect(surface,(255,255,255),rectout)
         pygame.draw.rect(surface,(0,0,0),rectin)
         
      if self.mouseover:
         pygame.draw.rect(surface,self.hilight,self.rect)
      else:
         pygame.draw.rect(surface,self.normal,self.rect)
      surface.blit(self.text_image,self.text_pos)
      
   def Update(self,event):
      x,y = event.pos
      px,py,w,h = self.rect
      self.mouseover = False
      if x > px and x < px + w:
         if y > py and y < py + h:
            self.mouseover = True
      if not self.mouseover:
         self.buttondown = False
   
   def MouseDown(self,event):
      if self.mouseover:
         self.buttondown = True
            
   def Click(self,event):
      # let you know when mouse is over button and button was push.
      if self.buttondown and self.mouseover:
         self.buttondown = False
         frame.push = frame.font.render('Click ' + self.text,1,(100,0,200))
         #print('You click %s' % (self.text))

class Main:
   def __init__(self):
      self.button = Button('Button 1',(50,50))
      self.button2 = Button('Button 2',(175,50),(100,30),(200,0,0),(200,0,200))
      self.button3 = Button('Button 3',(300,50),color=(0,200,0),hilight=(200,200,0))
      
      self.font = pygame.font.Font(None,18)
      self.push = None
   
   def Update(self,surface):
      surface.fill((150,200,150))
      # draw background here.
      self.button.Draw(surface)
      self.button2.Draw(surface)
      self.button3.Draw(surface)
      
      if self.push is not None:
         surface.blit(self.push,(100,100))
      
   def Event(self,event):
      if event.type == pygame.MOUSEBUTTONDOWN:
         self.button.MouseDown(event)
         self.button2.MouseDown(event)
         self.button3.MouseDown(event)
      elif event.type == pygame.MOUSEBUTTONUP:
         self.button.Click(event)
         self.button2.Click(event)
         self.button3.Click(event)
      elif event.type == pygame.MOUSEMOTION:
         self.button.Update(event)
         self.button2.Update(event)
         self.button3.Update(event)
               
if __name__ == '__main__':
   window = Window('Basic Pygame Window',(800,600))
   frame = Main()
   window.SetPage(frame.Update,frame.Event)
   window.Flip()
   pygame.quit()