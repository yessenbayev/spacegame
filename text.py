from __future__ import absolute_import, division, print_function, unicode_literals
from init import *
import pygame

def text_objects(text,font,size,color):
    '''Parses text to gameDisplay.blit(TextSurf,TextRect)'''
    font = pygame.font.Font(font,size)
    TextSurf = font.render(text, True, color)
    TextRect = TextSurf.get_rect()
    return TextSurf, TextRect

GameOverSurf, GameOverRect = text_objects('Game Over',
                                          'freesansbold.ttf',
                                          115,(255,255,255))
GameOverRect.center = (display_width/2,display_height/2)

GameOverSurf2, GameOverRect2 = text_objects('Press SPACE to start the game again',
                                          'freesansbold.ttf',
                                          50,(255,255,255))
GameOverRect2.center = (display_width/2,display_height/2+100)

def print_score(score,GameOver):
    ts, tr = text_objects('{} Score'.format(score),'freesansbold.ttf',
                          50, (255,255,255))
    tr.topright = (display_width,0)
    gameDisplay.blit(ts,tr)

    if GameOver:
        GameOverSurf, GameOverRect = text_objects('Score: {}'.format(score),
                                          'freesansbold.ttf',
                                          50,(255,255,255))
        GameOverRect.center = (display_width/2,display_height/2-100)
        gameDisplay.blit(GameOverSurf,GameOverRect)
