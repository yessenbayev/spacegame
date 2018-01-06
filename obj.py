from init import *
import pygame
import glob

def load_sprites(sprite_dir='.'):
        li = []
        if type(sprite_dir)==pygame.Surface:
                return sprite_dir
        for i in glob.glob(sprite_dir + "/*.png"):
            li.append(pygame.image.load(i))
        return li

def intersect(r,b):
        '''r is a rocket object, b is a block object'''
        rx1 = r.x + r.x1
        rx2 = r.x + r.x2
        ry1 = r.y + r.y1
        ry2 = r.y + r.y2
        if r.Hit == False:
                if b.x<rx1<(b.x+b.width) or b.x<rx2<(b.x+b.width):
                        if b.y<ry1<(b.y+b.height) or b.y<ry2<(b.y+b.height):
                                return True
        return False

class GameObject(object):
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

class Sprite(GameObject):
        def __init__(self,x,y,dx,dy,sprites):
                GameObject.__init__(self,x,y,dx,dy)
                self.sprites = sprites

        def display(self,i):
                self.x += self.dx
                self.y += self.dy
                gameDisplay.blit(self.sprites[i],(self.x,self.y))
                        
class block(Sprite): #any block 
        def __init__(self,sprite,x,y,dx,dy,width,height):
                Sprite.__init__(self,x,y,dx,dy,sprite)
                self.width = width
                self.height = height

        def display(self):
                self.x += self.dx
                self.y += self.dy
                gameDisplay.blit(self.sprites[0],(self.x,self.y))

class laser(block):
        def __init__(self,sprite,x,y,dx,dy,width,height,parent):
                block.__init__(self,sprite,x,y,dx,dy,width,height)
                self.parent = parent

class rock(block):
        def __init__(self,start_y):
                block.__init__(self,load_sprites('./media/graphics/rock'),
                               display_width,start_y,-20,0,200,100)

class rocket(Sprite):
    def __init__ (self,sprites,laser_sprites,HP,x1,x2,y1,y2,x,y,dx=0,dy=0):
                Sprite.__init__(self,x,y,dx,dy,sprites)
                self.laser_sprites = laser_sprites
                self.HP = HP
                self.x1 = x1 #these four coordinates define the block
                self.x2 = x2 #on the image that corresponds to the
                self.y1 = y1 #hit box
                self.y2 = y2

    def shot(self):
        '''Shooting straight with speed 50px'''
        dx = 50
        dy = 0
        width = 100
        height = 50
        return laser(self.laser_sprites,
                     (self.x+self.x2),
                     (self.y+(self.y1+self.y2)/2),
                     dx,dy,width,height,self)

    def display(self):
        i = max(min(len(self.sprites)-1,self.HP),0)
        Sprite.display(self,i)
        
class player_class(rocket):
    def __init__(self,x,y):
            rocket.__init__(self,load_sprites('./media/graphics/player/small'),
                            load_sprites('./media/graphics/lasers/player'),
                            3,130,275,40,165,x,y)
            self.Hit = False
            self.j = 0

    def hit(self):
            self.HP -= 1
            self.Hit = True

    def display(self):
            self.x += self.dx
            self.y += self.dy
            if self.Hit == True:
                    self.j += 1
                    if self.j == 30:
                            self.Hit = False
                            self.j = 0
            if self.Hit == False or self.j%2==0:
                    i = max(min(len(self.sprites)-1,self.HP),0)
                    gameDisplay.blit(self.sprites[i],(self.x,self.y))

class enemy(rocket):
    pass

