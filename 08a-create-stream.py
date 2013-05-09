"""
Set up a streaming server.
"""

import time
import SimpleCV

cam = SimpleCV.Camera()
js = SimpleCV.JpegStreamer('0.0.0.0:8080')

while True:
    cam.getImage().save(js.framebuffer)
    time.sleep(0.1)
