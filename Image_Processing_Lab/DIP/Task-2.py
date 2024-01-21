import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Task-2(a) starts here
def task_2a():
    gray_img = cv.imread('images/pic-1.jpg', 0)
    img = cv.resize(gray_img, (512,512))
    h,w = img.shape
    plt.subplot(1,2,1)
    plt.imshow(img, cmap= 'gray')
    plt.title('Original Image')
    for i in range(h):
        for j in range (w):
            if 127<img[i,j]<256:
                img[i,j]=255
           
    plt.subplot(1,2,2)
    plt.imshow(img, cmap= 'gray')
    plt.title('Enhanced Image')

    plt.tight_layout()
    plt.show()
# Task-2(a) ends here

# ***************************************************************** #
# Task-2(b) starts here
def task_2b():
    white_img = cv.resize(cv.imread('images/myimg1.jpg', 0), (512,512))
    plt.subplot(2,3,1)
    plt.imshow(white_img, cmap='gray')
    plt.title('Original Image')

    gamma = 0.5
    power_img = white_img**gamma
    plt.subplot(2,3,2)
    plt.imshow(power_img, cmap='gray')
    plt.title(f'gamma = {gamma}')

    gamma = 5.5
    power_img = white_img**gamma
    plt.subplot(2,3,3)
    plt.imshow(power_img, cmap='gray')
    plt.title(f'gamma = {gamma}')

    temp = white_img/256
    power_img = 10**temp
    plt.subplot(2,3,4)
    plt.imshow(power_img, cmap='gray')
    plt.title(f'Inverse Log Image')

    power_img = np.log(1+white_img)
    plt.subplot(2,3,5)
    plt.imshow(power_img, cmap='gray')
    plt.title(f'Log Image')

    plt.tight_layout()
    plt.show()
# Task-2(b) ends here

# ***************************************************************** #
# Task-2(c) starts here
def task_2c():
    gray_img = cv.resize(cv.imread('Images/shaun.jpg', cv.IMREAD_GRAYSCALE), (512,512))
    plt.subplot(1,2,1)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Original Image')
    new_img = gray_img & 224
    plt.subplot(1,2,2)
    plt.imshow(new_img, cmap='gray')
    plt.title('MSB 8 bit image')

    plt.show()
    plt.tight_layout()
# Task-2(c) ends here


def main():
    # task_2a()
    task_2b()
    # task_2c()

if __name__ == '__main__':
    main()