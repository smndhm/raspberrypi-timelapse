#!/usr/bin/python

from time import sleep
from datetime import datetime, timedelta
import sys
import os
import picamera

#default
interval_default = 10
duration_default = 60
usb_folder = False

#init camera
camera = picamera.PiCamera()
camera.resolution = (1640, 1232)
#extra camera setting
#camera.resolution = camera.MAX_RESOLUTION
#camera.hflip = True
#camera.vflip = True
#camera.rotation = 90

#check arguments
if len(sys.argv) > 1:
	project  = sys.argv[1]
	interval = interval_default if len(sys.argv) <= 2 else sys.argv[2]
	duration = duration_default if len(sys.argv) <= 3 else sys.argv[3]
	usb_folder  = False if len(sys.argv) <= 4 or not os.path.isdir('/media/usb/' + sys.argv[4]) else True
else:
	project  = raw_input("Project name: ")
	interval = input("Picture interval: ")
	duration = input("Timelapse length: ")

#make
if usb_folder:
	path = '/media/usb/' + sys.argv[4] + '/' + project + '/'
else:
	path = os.path.dirname(os.path.realpath(__file__)) + '/' + project + '/'

if not os.path.isdir(path):
	os.makedirs(path)
	os.chmod(path, 0777)

print "camera warm-up..."
sleep(2)

timestamp = datetime.now()
timestamp_end = timestamp + timedelta(seconds=(int(duration) * 60))

for filename in camera.capture_continuous(path + '{counter:04d}.jpg'):
	print('Captured %s' % filename)
	timestamp = timestamp + timedelta(seconds=int(interval))
	wait = timestamp - datetime.now()
	sleep(wait.seconds + wait.microseconds/1E6)
