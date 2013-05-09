import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    img = cam.getImage()
    h = img.sideBySide(
        img.flipHorizontal()
    )
    h.sideBySide(
        h.flipVertical(),
        'top'
    ).save(disp)

    if disp.lastLeftButton:
        break
