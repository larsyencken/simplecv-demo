import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    img = cam.getImage()
    leftright = img.sideBySide(
        img.flipHorizontal()
    )
    leftright.sideBySide(
        leftright.flipVertical(),
        'top'
    ).save(disp)

    if disp.lastLeftButton:
        break
