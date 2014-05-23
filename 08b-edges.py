import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    # use Canny edge detection algorithm
    img = cam.getImage().edges()
    img.save(disp)

    if disp.lastLeftButton:
        break
