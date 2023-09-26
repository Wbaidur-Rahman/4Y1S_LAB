import cv2
import math
import numpy as np
import matplotlib.pyplot as plt


image_path = 'im2.jpg'

def main():

    image = cv2.imread(image_path) #loading image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #converting to gray

    plt.subplot(2,1,1)
    plt.imshow(image, cmap='gray')

    h,w = image.shape

    gamma = 0.6

    image = image / 255


    for i in range(0,h):
        for j in range(0,w):
            image[i,j] = image[i,j] ** gamma
            # image[i,j] = int(math.pow(10,image[i,j])-1)
            # image[i,j] = math.log(1+image[i,j])

    image = image * 255

    plt.subplot(2,1,2)
    plt.imshow(image, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()