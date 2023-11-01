# This program is an illustration of the histogram of the image 

import cv2
import numpy as np
import matplotlib.pyplot as plt

Gray_img = cv2.imread('pic-1.jpg',0)
img = cv2.resize(Gray_img, (512,512))

h,w = img.shape

def histogram(img, levels):
    x = np.zeros(levels, dtype=int)
    h,w = img.shape
    for i in range(h):
        for j in range(w):
            x[img[i,j]]+=1
    return x


plt.subplot(3,1,1)
plt.bar(range(256), histogram(img, 256))
plt.ylabel('Normalized Frequency')
plt.title('Histogram 1')

img = (img>128)*255

plt.subplot(3,1,2)
plt.bar(range(256), histogram(img,256))
plt.title('Histogram 2')

plt.subplot(3,1,3)
plt.imshow(img, cmap='gray')
plt.title('Threshold Image')

plt.show()

