"""
Save images in preparation for a time lapse shot.
"""

import os
import SimpleCV
import time

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

os.mkdir('timelapse')

i = 0
while disp.isNotDone():
    time.sleep(1)

    img = cam.getImage()
    img.save(disp)
    img.save('timelapse/%.06d.jpg' % i)

    i += 1

    if disp.lastLeftButton:
        break
