import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

prev = cam.getImage().toGray()
while disp.isNotDone():
    img = cam.getImage().toGray()
    diff = (img - prev)
    diff.save(disp)

    prev = img

    if disp.lastLeftButton:
        break
