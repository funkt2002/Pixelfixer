# Pixelfixer
corrects color for 'corrupted' pixels in image
pixdetect.py creates an array of all of the pixels in the image and then locates which pixels have an rbg value of [255,0,00]-signifying they are read. 
Then it returns the locations of each red pixel. 
pixelfixer.py first locates all of the red pixels in the image, and then it finds the left, right, above, and bottom neighbors. It then takes the RGB values of each neighboring pixels and averages them. This average then replaces the 'corrupted' red pixel. This is done repititvely with a for loop through an array of all of the pixels. 
There is then a new file created of the image with all of the red pixels replaced with the averaged values. 
