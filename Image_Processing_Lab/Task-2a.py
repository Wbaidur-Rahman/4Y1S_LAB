import cv2
import matplotlib.pyplot as plt
import numpy as np

Color_img = cv2.imread('butterfly.jpg')
Gray_img = cv2.cvtColor(Color_img, cv2.COLOR_BGR2GRAY)
Image = cv2.resize(Gray_img,(512,512))
Re_color = cv2.cvtColor(Gray_img,cv2.COLOR_GRAY2RGB)
New_img = cv2.resize(Re_color,(512,512))

print(Image[100])
print('Difference\n')
print(New_img[100:101])

plt.subplot(2,1,1)
plt.imshow(Image,cmap='gray')

plt.subplot(2,1,2)
plt.imshow(New_img)

plt.show()

