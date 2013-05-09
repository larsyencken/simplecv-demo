import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    img = cam.getImage()
    img.save(disp)

    if disp.lastLeftButton:
        break
