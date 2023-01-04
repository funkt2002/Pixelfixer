import numpy as np
import cv2


def pixeldetect():

    I=cv2.imread('corruptedmoon.png')
    red_pixels = np.array(I)
    np.argwhere((red_pixels==[255,0,0]).all(axis=2))
    cv2.imwrite('corruptedmoon.png',I)
    return I
#



pixeldetect()
print('urmom')