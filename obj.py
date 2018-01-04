from init import *
import pygame
import glob

def load_sprites(sprite_dir='.'):
        li = []
        print(sprite_dir)
        if type(sprite_dir)==pygame.Surface:
                return sprite_dir
        for i in glob.glob(sprite_dir + "/*.png"):
            li.append(pygame.image.load(i))
        return li

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
        pass

class rocket(Sprite):
    def __init__ (self,sprites,laser_sprites,HP,x,y,dx=0,dy=0):
                Sprite.__init__(self,x,y,dx,dy,sprites)
                self.laser_sprites = laser_sprites
                self.HP = HP

    def shot(self):
        '''Shooting straight with speed 50px'''
        dx = 50
        dy = 0
        width = 100
        height = 50
        return laser(self.laser_sprites,self.x,self.y,dx,dy,width,height)

    def display(self):
        i = max(min(len(self.sprites)-1,self.HP),0)
        Sprite.display(self,i)
        
class player_class(rocket):
    def __init__(self,sprites,laser_sprites,x,y):
            rocket.__init__(self,sprites,laser_sprites,3,x,y)

class enemy(rocket):
    pass

