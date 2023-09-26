# This program will read an image as numpy array and then change its intensity resolution

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

Color_img = cv2.imread('im2.jpg',1)
print(Color_img.shape)
Color_img = cv2.resize(Color_img,(512,512))
Gray_img = cv2.cvtColor(Color_img,cv2.COLOR_BGR2GRAY)

samples = 7
h,w = Gray_img.shape

plt.subplot(3,3,1)
plt.imshow(Gray_img,cmap='gray')
plt.title('Original')

original = Gray_img.copy()

for s in range (samples):
    delta = 255//(math.pow(2,s+1))+1
    Gray_img = original.copy()
    for i in range (h):
        for j in range (w):
            # Gray_img[i,j] &= 2**(s+1)-1
            Gray_img[i,j] = (original[i,j]//delta)*delta
    plt.subplot(3,3,s+2)
    plt.imshow(Gray_img,cmap='gray')
    plt.title('Image {}'.format(s+1))
plt.show()
