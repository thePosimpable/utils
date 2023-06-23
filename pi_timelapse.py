from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.rotation = 180
camera.resolution = (2592, 1944)
camera.brightness = 60


camera.start_preview()
for counter in range(5):
	dateTimeObj = datetime.now()
	camera.capture('%s-%s-%s_%s_%s_%s.jpg' % (dateTimeObj.year, dateTimeObj.month, dateTimeObj.day, dateTimeObj.hour, dateTimeObj.minute, dateTimeObj.second))
	sleep(5)

camera.stop_preview()
