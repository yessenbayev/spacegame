from __future__ import absolute_import, division, print_function, unicode_literals
import pygame

display_width = 1366
display_height = 768

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Space')
clock = pygame.time.Clock()
