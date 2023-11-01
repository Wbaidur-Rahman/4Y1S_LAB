# This program will read an image as numpy array and then change its intensity resolution

import cv2
import numpy as np
import matplotlib.pyplot as plt

Gray_img = cv2.imread('shaun.jpg',0)
# Gray_img = cv2.resize(Color_img,(512,512))

samples = 7
h,w = Gray_img.shape

plt.subplot(3,3,1)
plt.imshow(Gray_img,cmap='gray')
plt.title('Original')

original = Gray_img.copy()

for s in range (samples):
    Gray_img = original.copy()
    for i in range (h):
        for j in range (w):
            Gray_img[i,j] = np.floor((Gray_img[i,j]/256)*(2**(s+1)))
    plt.subplot(3,3,s+2)
    plt.imshow(Gray_img,cmap='gray')
    plt.title(f'{s+1} bit image')
plt.show()
