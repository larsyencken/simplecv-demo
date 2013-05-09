import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))


def print_motion(m):
    print int(m / 15) * '*'


last = cam.getImage()
w, h = last.size()
total = w * h
while disp.isNotDone():
    img = cam.getImage().toGray()
    diff = (img - last).binarize(10).invert().erode(4).dilate(5)
    diff.save(disp)
    motion = diff.getNumpy().sum() / float(total)
    print_motion(motion)

    last = img

    if disp.lastLeftButton:
        break
