import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    img = cam.getImage()
    mask = img.getSkintoneMask(0)
    img.sideBySide(mask).save(disp)

    if disp.lastLeftButton:
        break
