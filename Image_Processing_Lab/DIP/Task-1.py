import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Task 1(a) starts here
def task_1a():
    gray_img = cv.imread('images/shaun.jpg', 0)
    img = cv.resize(gray_img, (512, 512))
    count = 1
    plt.subplot(3,3,count) 
    plt.imshow(img, cmap='gray')
    count+=1
    h,w=img.shape

    plt.title('Shaun')
    plt.xlabel(f'{512} bit image')


    while h>4:
        h,w=img.shape
        new_img = np.zeros(((h//2, w//2)), dtype= np.uint8)
        for i in range (0, h , 2):
            for j in range (0, w, 2):
                new_img[i//2, j//2] = img[i,j]
        img = new_img
        plt.subplot(3,3,count) 
        plt.imshow(img, cmap='gray')
        plt.title('Shaun')
        plt.xlabel(f'{h//2} bit image')
        count+=1
    plt.tight_layout()
    plt.show()
# Task-1(a) ends here

#******************************************************************************#
# Task-1(b) starts here
def task_1b():
    gray_img = cv.imread('images/shaun.jpg', 0)
    img = cv.resize(gray_img, (512,512))
    count = 1
    plt.subplot(3, 3, count)
    plt.imshow(img, cmap='gray')
    plt.title('Shaun')
    plt.xlabel(f'{256} level image')
    count+=1

    level = 256
    h,w = img.shape

    while level>2:
        for i in range (h):
            for j in range (w):
                img[i,j] = (int)((img[i,j]/level)*(level//2))
        level//=2
        plt.subplot(3, 3, count)
        plt.imshow(img, cmap='gray')
        plt.title('Shaun')
        plt.xlabel(f'{level} level image')
        count+=1
    plt.tight_layout()
    plt.show()
# Task-1(b) ends here

#******************************************************************************#
# Task-1(c) starts here
def task_1c():
    gray_img = cv.imread('images/pic-1.jpg', 0)
    # gray_img = np.asarray([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,6,6,6,6,6,6,6])
    img = cv.resize(gray_img, (200,200))
    plt.subplot(1,3,1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.subplot(1,3,2)
    plt.hist(gray_img, 64, ((0,255)))
    plt.xlabel('Histogram')
    img=img>127
    plt.subplot(1,3,3)
    plt.imshow(img, cmap='gray')
    plt.title('Thresholding')
    plt.xlabel('Image after segmentation')
    plt.tight_layout()
    plt.show()
# Task-1(c) ends here

def main():
    # task_1a()
    # task_1b()
    task_1c()

if __name__ == '__main__':
    main()