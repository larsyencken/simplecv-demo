"""
Cycle between eroding and dilating the current image.
"""

import SimpleCV


def erode_or_dilate(img, n):
    """
    Erode or dilate an image by n, depending on whether n is positive or
    negative. When n is 0, then image is returned unchanged.
    """
    if n < 0:
        return img.erode(-n).dilate(-n)
    if n > 0:
        return img.dilate(n).erode(n)

    return img


cycle = range(-8, 9) + range(7, -8, -1)
start = 8

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

i = start
j = 0
while disp.isNotDone():
    img = cam.getImage()
    img = erode_or_dilate(img, cycle[i % len(cycle)])
    img.save(disp)

    if disp.lastLeftButton:
        break

    j += 1

    if j % 10 == 0:
        i += 1
