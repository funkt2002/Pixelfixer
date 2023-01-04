#--------------------command line utility fixes corrupted pixels in RGB images-
import argparse
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description='direct code based on user input')  #
parser.add_argument('image_file', help='finds the image with corrupted pixels and directs the code to this file')
parser.add_argument('--fix', choices=['average', 'filter'], default='average',
                    help='option for fixing the corrupted pixels. average will take the avg RGB vals of the surrounding pixels '
                         'replace corrupted pixel with it \
                       . filter: corrupted pixels are just replaced with black pixels.')


args = parser.parse_args()
image_file = args.image_file
fix = args.fix


def find_pixels(img):
    # this is gonna set each color of pix
    img_r = img[:,:,0]
    img_g = img[:,:,1]
    img_b = img[:,:,2]
    pixels = ((img_r == 1) & (img_g == 0) & (img_b == 0))
    return pixels


def pixfix(img, pixels):#this is finding neighbors RGB vals and replacing corrupting pics
#the for loop goes through the array and finds a neighbor, and then changes RGB vals with the means of them 
    img_r = img[:,:,0]
    img_g = img[:,:,1]
    img_b = img[:,:,2]
    dim0, dim1 = np.nonzero(pixels)
    for r, c in zip(dim0, dim1):
        # up neighbor
        if r == 0 and c > 0:
            mean_r = np.mean([img_r[r+1,c], img_r[r,c+1], img_r[r,c-1]])
            mean_g = np.mean([img_g[r+1,c], img_g[r,c+1], img_g[r,c-1]])
            mean_b = np.mean([img_b[r+1,c], img_b[r,c+1], img_b[r,c-1]])
            img_r[r,c] = mean_r
            img_g[r,c] = mean_g
            img_b[r,c] = mean_b
        # left neighbor
        elif r > 0 and c == 0:
            mean_r = np.mean([img_r[r+1,c], img_r[r,c+1], img_r[r-1,c]])
            mean_g = np.mean([img_g[r+1,c], img_g[r,c+1], img_g[r-1,c]])
            mean_b = np.mean([img_b[r+1,c], img_b[r,c+1], img_b[r-1,c]])
            img_r[r,c] = mean_r
            img_g[r,c] = mean_g
            img_b[r,c] = mean_b
        # middle-center(the pix)
        elif r+1 < img_r.shape[0] and c+1 < img_r.shape[1]:
            mean_r = np.mean([img_r[r+1,c], img_r[r,c+1], img_r[r,c-1], img_r[r-1,c]])
            mean_g = np.mean([img_g[r+1,c], img_g[r,c+1], img_g[r,c-1], img_g[r-1,c]])
            mean_b = np.mean([img_b[r+1,c], img_b[r,c+1], img_b[r,c-1], img_b[r-1,c]])
            img_r[r,c] = mean_r
            img_g[r,c] = mean_g
            img_b[r,c] = mean_b
        # right neighbor
        elif r > 0 and c == img_r.shape[1]:
            mean_r = np.mean([img_r[r+1,c], img_r[r,c-1], img_r[r-1,c]])
            mean_g = np.mean([img_g[r+1,c], img_g[r,c-1], img_g[r-1,c]])
            mean_b = np.mean([img_b[r+1,c], img_b[r,c-1], img_b[r-1,c]])
            img_r[r,c] = mean_r
            img_g[r,c] = mean_g
            img_b[r,c] = mean_b
        # down neighbor
        elif r == img_r.shape[0] and c > 0:
            mean_r = np.mean([img_r[r,c+1], img_r[r,c-1], img_r[r-1,c]])
            mean_g = np.mean([img_g[r,c+1], img_g[r,c-1], img_g[r-1,c]])
            mean_b = np.mean([img_b[r,c+1], img_b[r,c-1], img_b[r-1,c]])
            img_r[r,c] = mean_r
            img_g[r,c] = mean_g
            img_b[r,c] = mean_b

    img[:,:,0] = img_r
    img[:,:,1] = img_g
    img[:,:,2] = img_b
    return img



def pixreplace(img, pixels):
    img_r = img[:,:,0]
    img_r[pixels] = 0
    img[:,:,0] = img_r
    return img

#parses da file and creates the new file name
img = plt.imread(image_file)
pixels = find_pixels(img)
file_name = image_file.split("/")[-1]
file_name_new = file_name.split(".")[0] + "_fixed." + file_name.split(".")[-1]

# Wasn't sure honestly how to properly use ARGSPARSE for optional argsfor this lol and the if made sense to me so here it is lol
if fix == "average":
    img_new = pixfix(img.copy(), pixels)
else:
    img_new = pixreplace(img.copy(), pixels)

plt.imsave(file_name_new, img_new)
plt.imshow(file_name_new, img_new)








