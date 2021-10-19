import numpy as np
import math
from PIL import Image


im = Image.open('pong.png')
im.show()

array=np.array(im)
print(array.shape)
print(array)
