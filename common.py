#
#  common.py
#
#  Render an image inline in IPython.
#

import tempfile

def render_image(i):
    n = tempfile.NamedTemporaryFile(suffix='.png')
    i.save(n)
    return open(n.name).read()

Image._repr_png_ = lambda i: render_image(i)
