#!/usr/bin/env python

# Imports
import sys
import os

import RPi.GPIO as GPIO

import pygame
import pygame.camera
from pygame.locals import *

# 
dirname = os.path.dirname(os.path.realpath(__file__))
print dirname

# Init GPIO
print('Init GPIO...')
GPIO.setmode(GPIO.BCM)
gpioButtons = {
	21:'Button 1/GPIO',
	20:'Button 2/GPIO',
	16:'Button 3/GPIO',
	6:'Joystick Up',
	19:'Joystick Down',
	5:'Joystick Left',
	26:'Joystick Right',
	13:'Joystick Press'
}
for i in gpioButtons.keys():
 GPIO.setup(i, GPIO.IN, pull_up_down = GPIO.PUD_UP)


# Init Pygame
print('Init Pygame...')
pygame.init()
# pygame.mouse.set_visible(0)

# Init Font
print('Init Font...')
pygame.font.init()
font = pygame.font.Font(os.path.join(dirname, 'assets/fonts/LSLT-Regular.ttf'), 200)

# Init Camera
# print('Init camera...')
# camera_resolution_width = 1920
# camera_resolution_height = 1200
# camera_resolution = (camera_resolution_width, camera_resolution_height)

# camera_rotation = 90

# pygame.camera.init()
# cameras = pygame.camera.list_cameras()
# if len(cameras) == 0:
#  sys.exit("No camera")
# camera = pygame.camera.Camera(cameras[0], camera_resolution, "RGB")
# print(cameras[0], camera_resolution, camera_rotation)

# camera.start()


# Init Screen
# print('Init screen...')
# screen_resolution = (camera_resolution_width/2, camera_resolution_height/2)
# screen = pygame.display.set_mode(screen_resolution, pygame.FULLSCREEN)
# print(screen_resolution)

#display camera on screen
# camera_image = pygame.surface.Surface(camera_resolution)
# screen_image = pygame.surface.Surface(screen_resolution)

# while True:
#  if camera.query_image():
#   camera_image = camera.get_image(camera_image)
#  screen_image = pygame.transform.scale(camera_image, screen_resolution, screen_image)
#  screen.blit(pygame.transform.rotate(camera_image, camera_rotation), (0,0))
#  pygame.display.flip()

#home

clock = pygame.time.Clock()

default_screen_resolution = (1000, 1000)
screen = pygame.display.set_mode(default_screen_resolution, pygame.FULLSCREEN)

text = font.render("PRESS TO START", True, [255, 255, 255])
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery

screen.fill((0, 0, 0))
screen.blit(text, textrect)

pygame.display.update()

while True:
	clock.tick(20)
	for (k,v) in gpioButtons.items():
		if GPIO.input(k) == False:
			print v