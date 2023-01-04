from PIL import Image
import argparse
import matplotlib
import numpy as np
from numpy import asarray
from matplotlib import pyplot
def pixfix(path,name):
    I=matplotlib.pyplot.imread(path)
    image_array = np.array(I)
    new_image = image_array.copy()
    n = 0
    average_sum = 0
    for i in range(0, len(image_array)):
        for j in range(0, len(image_array[i])):
            for k in range(-2, 3):
                for l in range(-2, 3):
                    if (len(image_array) > (i + k) >= 0) and (len(image_array[i]) > (j + l) >= 0):
                        average_sum += image_array[i + k][j + l]
                        n += 1

            new_image[i][j] = ((average_sum / n))
            average_sum = 0
            n = 0

        pyplot.imsave(path,I)
        pyplot.imshow(path,I)
        pyplot.imshow()
        #x = Image.fromarray(np.array(new_image), 'L')
        #x.save(name)
        print("done")

pixfix('corruptedmoon.png','moonpic')
