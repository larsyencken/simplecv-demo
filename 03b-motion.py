import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

prev = cam.getImage()
while disp.isNotDone():
    img = cam.getImage().toGray()
    diff = (img - prev).binarize().invert()
    diff.save(disp)

    prev = img

    if disp.lastLeftButton:
        break
