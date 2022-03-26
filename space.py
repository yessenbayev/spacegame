from init import *
from obj import *
import text
import random
import sys

difficulty = 30

def rocks(scene):
        if random.randrange(0,difficulty)==0:
                start_y = random.randrange(0,display_height)
                scene.append(rock(start_y))

def screenedge(player):
        rx1 = player.x + player.x1
        rx2 = player.x + player.x2
        ry1 = player.y + player.y1
        ry2 = player.y + player.y2
        if (rx1 < 0 and player.dx < 0) or (rx2 > display_width and player.dx > 0):
                player.dx = 0
        if (ry1 < 0 and player.dy < 0) or (ry2 > display_height and player.dy > 0):
                player.dy = 0

def gameLoop():
    x = (display_width* 0.1)
    y = (display_height*0.5)
    player = player_class(x,y)
    running = True
    GameOver = False
    score = 0

    scene = [player]
    lasers = []
    while running:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                            pygame.quit()
                            sys.exit()

                    elif event.type == pygame.KEYDOWN:
                            if GameOver:
                                    if event.key == pygame.K_RETURN:
                                            gameLoop()
                            else:
                                    if event.key == pygame.K_a:
                                        player.dx = -10
                                    elif event.key == pygame.K_d:
                                        player.dx = 10
                                    if event.key == pygame.K_w:
                                        player.dy = -10
                                    elif event.key == pygame.K_s:
                                        player.dy = 10
                                    if event.key == pygame.K_SPACE:
                                        l = player.shot()
                                        scene.append(l)
                                        lasers.append(l)

                    elif event.type == pygame.KEYUP:
                            if event.key in (pygame.K_d,pygame.K_a):
                                    player.dx = 0
                            if event.key in (pygame.K_w,pygame.K_s):
                                    player.dy = 0
            screenedge(player)
            gameDisplay.fill((0,0,0))
            if not GameOver:
                    rocks(scene)
            if player.HP <= 0:
                    GameOver = True
            for i in scene:
                if GameOver is True and type(i)!=laser:
                        i.dx = 0
                        i.dy = 0
                i.display()
                if type(i) in (laser,rock):
                        if type(i)==rock:
                                if intersect(player,i) and not GameOver:
                                        player.hit()
                                for j in lasers:
                                        if laser_intersect(j,i):
                                                scene.remove(i)
                                                scene.remove(j)
                                                lasers.remove(j)
                                                score += 1000
                                                break
                        if i.x >= display_width or i.x <= 0-i.width:
                                scene.remove(i)
                                if type(i)==laser:
                                        lasers.remove(i)
            text.print_score(score,GameOver)
            if GameOver:
                    gameDisplay.blit(text.GameOverSurf,
                                     text.GameOverRect)
                    gameDisplay.blit(text.GameOverSurf2,
                                     text.GameOverRect2)
            pygame.display.update()
            clock.tick(60)
            if not GameOver:
                    score += 1

gameLoop()
