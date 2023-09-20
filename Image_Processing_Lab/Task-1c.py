# This program is an illustration of the histogram of the image 

import cv2
import numpy as np
import matplotlib.pyplot as plt

Color_img = cv2.imread('butterfly.jpg',1)
Color_img = cv2.resize(Color_img,(512,512))
Gray_img = cv2.cvtColor(Color_img,cv2.COLOR_BGR2GRAY)

h,w = Gray_img.shape

plt.subplot(3,1,1)
plt.hist(Gray_img,16)
# plt.xlabel('Values')
plt.ylabel('Normalized Frequency')
plt.title('Histogram 1')

threshold_value=128

# Apply binary thresholding
# _, thresholded_image = cv2.threshold( Gray_img, threshold_value, 255, cv2.THRESH_BINARY)
Gray_img = Gray_img>128
thresholded_image=Gray_img.copy()

plt.subplot(3,1,2)
plt.hist(thresholded_image.ravel(), bins=2, range=(0, 1))
# plt.xlabel('Values')
plt.ylabel('Normalized Frequency')
plt.title('Histogram 2')

print(thresholded_image)


plt.subplot(3,1,3)
plt.imshow(thresholded_image,cmap='gray')

plt.show()

