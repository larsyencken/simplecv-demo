import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    # show output of sobel operator
    img = cam.getImage().sobel().binarize(15).invert()
    img.save(disp)

    if disp.lastLeftButton:
        break
