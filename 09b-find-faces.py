import SimpleCV
import numpy as np

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

black = SimpleCV.Image(np.zeros((200, 200)))
while disp.isNotDone():
    img = cam.getImage()
    faces = img.findHaarFeatures('face.xml')
    if faces:
        face = faces[0].crop().resize(w=200, h=200)
    else:
        face = black
    img.sideBySide(face).save(disp)

    if disp.lastLeftButton:
        break
