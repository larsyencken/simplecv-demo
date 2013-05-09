import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    im = cam.getImage()
    im20 = im.binarize(20)
    im40 = im.binarize(40)
    im80 = im.binarize(80)
    im120 = im.binarize(120)

    im20.sideBySide(im40).sideBySide(
        im80.sideBySide(im120),
        side='bottom'
    ).save(disp)

    if disp.lastLeftButton:
        break
