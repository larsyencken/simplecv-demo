import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    im = cam.getImage()
    im.binarize().save(disp)

    if disp.lastLeftButton:
        break
