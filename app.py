#!/usr/bin/env python

# Imports
import sys
import os

from gpiozero import Button

import pygame
import pygame.camera
from pygame.locals import *

## ----------------------------------------------------------------------------------------------------
## Class Screen
## ----------------------------------------------------------------------------------------------------
class Screen():
	#__init__
	def __init__(self):
		self.colors = {
			'white':(255,255,255), 
			'black':(0,0,0)
		}	
		self.default_screen_resolution = (1000, 1000)
		self.screen = pygame.display.set_mode(self.default_screen_resolution)
		self.home()

	# setBackgroundColor
	def setBackgroundColor(self, color):
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill(color)
		self.screen.blit(self.background, (0, 0))

	def home(self):
		# Background
		self.setBackgroundColor(self.colors['black'])
		# Text
		text = font.render("PRESS TO START", True, self.colors['white'])
		textrect = text.get_rect()
		textrect.centerx = self.screen.get_rect().centerx
		textrect.centery = self.screen.get_rect().centery
		self.screen.blit(text, textrect)
		# update screen
		pygame.display.flip()
		# Buttons
		btnKey1.when_pressed = self.pictureInterval
		btnKey2.when_pressed = self.pictureInterval
		btnKey3.when_pressed = self.pictureInterval
		btnJoystickUp.when_pressed = self.pictureInterval
		btnJoystickDown.when_pressed = self.pictureInterval
		btnJoystickleft.when_pressed = self.pictureInterval
		btnJoystickRight.when_pressed = self.pictureInterval
		btnJoystickPress.when_pressed = self.pictureInterval

	def pictureInterval(self):
		# Background
		self.setBackgroundColor(self.colors['white'])
		# Text
		
		# update screen
		pygame.display.flip()
		# Buttons

## ----------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------

# Dirname
dirname = os.path.dirname(os.path.realpath(__file__))
print('dirname', dirname)

# Init GPIO
print('Init GPIO...')
btnKey1 = Button(21)
btnKey2 = Button(20)
btnKey3 = Button(16)
btnJoystickUp = Button(6)
btnJoystickDown = Button(19)
btnJoystickleft = Button(5)
btnJoystickRight = Button(26)
btnJoystickPress = Button(13)

# Init Pygame
print('Init Pygame...')
pygame.init()
pygame.mouse.set_visible(0)

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
# home
print('Starting...')
screen = Screen()

clock = pygame.time.Clock()

while True:
	clock.tick(20)