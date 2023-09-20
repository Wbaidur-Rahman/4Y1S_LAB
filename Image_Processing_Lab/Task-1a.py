# This program will read a picture as numpy array and then down sample the image


import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('butterfly.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img = cv2.resize(img,(512,512))

for k in range (4):
    h = img.shape[0]
    w = img.shape[1]
    new_img = np.zeros((h//2, w//2, 3), dtype=np.uint8)

    for i in range (2,h,2):
        for j in range (2,w,2):
            new_img[i//2][j//2] = img[i][j]
    img = new_img
    plt.subplot(2,2,k+1)
    plt.imshow(img)
    plt.title('Butterfly')

plt.show()