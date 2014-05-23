"""
Consume a jpeg stream.
"""

import time
import SimpleCV

js = SimpleCV.JpegStreamCamera('http://127.0.0.1:8080/stream')
disp = SimpleCV.Display((1024, 768))

while disp.isNotDone():
    js.getImage().save(disp)
    time.sleep(0.1)

    if disp.lastLeftButton:
        break
