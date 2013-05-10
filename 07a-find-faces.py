import SimpleCV

cam = SimpleCV.Camera()
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    img = cam.getImage()
    faces = img.findHaarFeatures('face.xml') or []
    for face in faces:
        face.draw(SimpleCV.Color.GREEN)
    img.save(disp)

    if disp.lastLeftButton:
        break
