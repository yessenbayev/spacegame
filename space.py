from init import *
from obj import *
import random
import sys

def gameOver():

        pass
        

def gameLoop():
    x = (display_width* 0.5)
    y = (display_height*0.5)
    player = player_class(load_sprites('./media/graphics/player/small'),
                    load_sprites('./media/graphics/lasers/player'),x,y)
    running = True
                                 
    scene = [player]
    while running:

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            running = False
                            
                    elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                player.dx = -5
                            elif event.key == pygame.K_RIGHT:
                                player.dx = 5
                            if event.key == pygame.K_UP:
                                player.dy = -5
                            elif event.key == pygame.K_DOWN:
                                player.dy = 5
                            if event.key == pygame.K_SPACE:
                                scene.append(player.shot())

                    elif event.type == pygame.KEYUP:
                            if event.key in (pygame.K_RIGHT,pygame.K_LEFT):
                                    player.dx = 0
                            if event.key in (pygame.K_UP,pygame.K_DOWN):
                                    player.dy = 0

            gameDisplay.fill((255,255,255))
            if random.randrange(0,50)==0:
                start_y = random.randrange(0,display_height)
                scene.append(block(load_sprites('./media/graphics/rock'),
                                   display_width,start_y,-20,0,200,100))
            for i in scene:
                    print(type(i))
                    i.display()
                    if type(i) in (laser,block):
                        if i.x >= display_width or i.x <= 0-i.width:
                            scene.remove(i)
            
            pygame.display.update()
            clock.tick(60)

gameLoop()

pygame.quit()
sys.exit()
