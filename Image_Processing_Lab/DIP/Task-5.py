import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def erosion(img, mask):
    new_img = np.copy(img)
    m,n = mask.shape
    h,w = img.shape
    for i in range (m//2,h-m//2):
        for j in range (n//2,w-n//2):
            c=0
            ok = True
            for l in range (i-m//2,i+m//2):
                for r in range (j-n//2,j+n//2):
                    if mask[l-i+m//2,r-j+n//2] == 0:
                        continue
                    else:
                        c+=1
                        if img[l,r] == 0:
                            ok = False
            if ok == True:
                new_img[i,j]=1
            else:
                new_img[i,j]=0
    return new_img
                        
def dilation(img, mask):
    new_img = np.copy(img)
    m,n = mask.shape
    h,w = img.shape
    for i in range (m//2,h-m//2):
        for j in range (n//2,w-n//2):
            c=0
            ok = False
            for l in range (i-m//2,i+m//2):
                for r in range (j-n//2,j+n//2):
                    if mask[l-i+m//2,r-j+n//2] == 0:
                        continue
                    else:
                        c+=1
                        if img[l,r] == 1:
                            ok = True
            if ok == True:
                new_img[i,j]=1
            else:
                new_img[i,j]=0
    return new_img

# ******************************************************************* #
# Task-5(a) starts here
def task_5a():
    img = cv.resize(cv.imread('Images/im.png', cv.IMREAD_GRAYSCALE), (200,200))
    img = (img>127)*1
    mask = np.ones((7,7))

    new_img  = erosion(img, mask)
    plt.subplot(1,3,1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1,3,2)
    plt.imshow(new_img, cmap='gray')
    plt.title('Image After Erosion')

    new_img = dilation(img, mask)
    plt.subplot(1,3,3)
    plt.imshow(new_img, cmap='gray')
    plt.title('Image After Dilation')

    plt.tight_layout()
    plt.show()
# Task-5(a) ends here

# ******************************************************************* #
#  task-5(b) starts here
def task_5b():
    img = cv.resize(cv.imread('Images/openclose.png', cv.IMREAD_GRAYSCALE), (100,100))
    img=255-img
    img = (img>25)*1
    
    mask = np.ones((10,10))

    plt.subplot(1,3,1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    new_img  = erosion(img, mask)
    new_img = dilation(new_img, mask)
    plt.subplot(1,3,2)
    plt.imshow(new_img, cmap='gray')
    plt.title('Image After Opening')

    new_img = dilation(img, mask)
    new_img = erosion(new_img, mask)
    plt.subplot(1,3,3)
    plt.imshow(new_img, cmap='gray')
    plt.title('Image After Closing')

    plt.tight_layout()
    plt.show()
# Task-5(b) ends here

# ******************************************************************* #
#  task-5(c) starts here
def task_5c():
    img = cv.resize(cv.imread('Images/boundary.png', 0), (200,200))
    img=(img>127)*1

    plt.subplot(1,2,1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    mask = np.ones((7,7))
    new_img = img-erosion(img, mask)
    plt.subplot(1,2,2)
    plt.imshow(new_img, cmap='gray')
    plt.title('Image Boundary')

    plt.show()
    plt.tight_layout()


def main():
    # task_5a()
    # task_5b()
    task_5c()

if __name__=='__main__':
    main()