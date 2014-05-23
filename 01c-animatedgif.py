"""
Make an animated gif.
"""

import SimpleCV
import time

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

imset = SimpleCV.ImageSet()

i = 0
while disp.isNotDone():
    time.sleep(0.2)

    img = cam.getImage()
    small = img.scale(0.3)
    imset.append(small)
    img.save(disp)

    if disp.lastLeftButton:
        break

    i += 1

    if i >= 20:
        break

imset.save('animated.gif')
