#!/usr/bin/env python

#imports
import sys
import os

import pygame
import pygame.camera
from pygame.locals import *


#init Pygame
print('Init Pygame...')
pygame.init()
pygame.mouse.set_visible(0)

#init Font
print('Init Font...')
pygame.font.init()
font=pygame.font.Font(os.path.join("assets", "fonts", 'LSLT-Regular.ttf'), 200)

#init Camera
# print('Init camera...')
# camera_resolution_width=1920
# camera_resolution_height=1200
# camera_resolution=(camera_resolution_width, camera_resolution_height)

# camera_rotation=90

# pygame.camera.init()
# cameras=pygame.camera.list_cameras()
# if len(cameras) == 0:
#   sys.exit("No camera")
# camera=pygame.camera.Camera(cameras[0], camera_resolution, "RGB")
# print(cameras[0], camera_resolution, camera_rotation)

# camera.start()


#init Screen
print('Init screen...')
# screen_resolution=(camera_resolution_width/2, camera_resolution_height/2)
# screen=pygame.display.set_mode(screen_resolution, pygame.FULLSCREEN)
# print(screen_resolution)

#display camera on screen
# camera_image=pygame.surface.Surface(camera_resolution)
# screen_image=pygame.surface.Surface(screen_resolution)

# while True:
#   if camera.query_image():
#     camera_image=camera.get_image(camera_image)
#   screen_image=pygame.transform.scale(camera_image, screen_resolution, screen_image)
#   screen.blit(pygame.transform.rotate(camera_image, camera_rotation), (0,0))
#   pygame.display.flip()

#init buttons

#home

clock = pygame.time.Clock()

default_screen_resolution=(1000, 1000)
screen = pygame.display.set_mode(default_screen_resolution, pygame.FULLSCREEN)

text=font.render("PRESS TO START", True, [255, 255, 255])
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery

screen.fill((0, 0, 0))
screen.blit(text, textrect)

pygame.display.update()

while True:
	clock.tick(20)