import cv2
import matplotlib.pyplot as plt
import numpy as np

Color_img = cv2.imread('shaun.jpg')
Gray_img = cv2.cvtColor(Color_img, cv2.COLOR_BGR2GRAY)
image = cv2.resize(Gray_img,(512,512))

plt.subplot(2,1,1)
plt.imshow(image,cmap='gray')

h,w = image.shape

for i in range (h):
    for j in range (w):
        if image[i,j]>=100 and image[i,j]<=200:
            image[i,j]=0

plt.subplot(2,1,2)
plt.imshow(image, cmap='gray')

plt.show()

