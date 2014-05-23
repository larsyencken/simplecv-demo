import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))


last = cam.getImage().toGray()

w, h = last.size()
num_pixels = w * h

while disp.isNotDone():
    img = cam.getImage().toGray()

    diff = (img - last).binarize(10).invert().erode(4).dilate(5)

    motion = diff.getNumpy().sum() / (255 * float(num_pixels))

    diff.drawText('%.00f' % (100 * motion), color=(255, 50, 50),
                  fontsize=140)

    diff.save(disp)

    last = img

    if disp.lastLeftButton:
        break
