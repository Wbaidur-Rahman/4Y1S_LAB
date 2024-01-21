import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def psnr(img, noisy_img):
    mse = np.mean((img-noisy_img)**2)
    x = 255.0
    if mse==0:
        return 100
    else:
        return 20*np.log(x/np.sqrt(mse))

def average_filter(img, mask_size):
    new_img = np.zeros((img.shape), dtype=np.uint8)
    h,w = img.shape
    for i in range (h):
        for j in range (w):
            x = 0
            y = 0
            for l in range (i-mask_size//2,i+(mask_size-1)//2):
                for r in range (j-mask_size//2,j+(mask_size-1)//2):
                    if -1<l<h and -1<r<w:
                        x+=img[l,r]
                        y+=1
            new_img[i,j]=x/max(y,1)
    return new_img

def median_filter(img, k):
    new_img = np.zeros((img.shape), dtype=np.uint8)
    h,w = img.shape
    for i in range (k//2,h-k//2):
        for j in range (k//2,w-k//2):
            new_img[i,j] = np.median(img[i-k//2:i+k//2,j-k//2:j+k//2])
    return new_img

def geometric_mean_filter(img, m):
    img=img/256
    new_img = np.copy(img)
    h,w = img.shape
    for i in range (m//2,h-m//2):
        for j in range (m//2,w-m//2):
            x=1
            for l in range (i-m//2,i+m//2):
                for r in range (j-m//2,j+m//2):
                    x*=(1+img[l,r])
            new_img[i,j]=x**(1/m**2)

            # new_img[i,j]=(np.prod((img[i-m//2:i+m//2,j-m//2:j+m//2])))**(1/m*m)
    return new_img

def harmonic_mean_filter(img, m):
    new_img = np.zeros(img.shape)
    img=img/256
    h,w = img.shape
    for i in range (m//2,h-m//2):
        for j in range (m//2,w-m//2):
            x=0.01
            for l in range (i-m//2,i+m//2):
                for r in range (j-m//2,j+m//2):
                    x+=1/(img[l,r]+1)
            new_img[i,j]=(m**2)/x
        # new_img[i,j]=(m*m)/(np.sum(1/img[i-m//2:i+m//2,j-m//2:j+m//2])+0.01)
    return new_img

# ******************************************************************************* #
# Task-3(a) starts here
def task_3a():
    img = cv.resize(cv.imread('Images/shaun.jpg', cv.IMREAD_GRAYSCALE), (512, 512))
    plt.subplot(2,2,1)
    plt.imshow(img, cmap='gray')
    plt.title('Original image')

    noisy_img = np.copy(img)
    x=10000
    while x!=0:
        i = np.random.randint(0,512)
        j = np.random.randint(0,512)
        noisy_img[i,j] = 255
        x-=1
    x = 1e4
    while x!=0:
        i = np.random.randint(0,512)
        j = np.random.randint(0,512)
        noisy_img[i,j] = 0
        x-=1

    plt.subplot(2,2,2)
    plt.imshow(noisy_img, cmap='gray')
    plt.title('Noisy image')

    filtered_img = average_filter(noisy_img, 5)
    plt.subplot(2,2,3)
    plt.imshow(filtered_img, cmap='gray')
    plt.title('Average filtered image')

    print(f'Average filter psnr ={psnr(img, filtered_img)}')

    filtered_img = median_filter(noisy_img, 5)
    plt.subplot(2,2,4)
    plt.imshow(filtered_img, cmap='gray')
    plt.title('Median filtered image')
    print(f'Median filter psnr = {psnr(img, filtered_img)}')

    plt.tight_layout()
    plt.show()
# Task-3(a) ends here

# ******************************************************************************* #
# Task-3(b) starts here
def task_3b():
    img = cv.resize(cv.imread('Images/shaun.jpg', cv.IMREAD_GRAYSCALE), (512, 512))

    noisy_img = np.copy(img)
    x=10000
    while x!=0:
        i = np.random.randint(0,512)
        j = np.random.randint(0,512)
        noisy_img[i,j] = 255
        x-=1
    x = 1e4
    while x!=0:
        i = np.random.randint(0,512)
        j = np.random.randint(0,512)
        noisy_img[i,j] = 0
        x-=1

    filtered_img1 = average_filter(noisy_img, 3)
    filtered_img2 = average_filter(noisy_img, 5)
    filtered_img3 = average_filter(noisy_img, 7)
    
    print(f'Average filter psnr with mask 3 = {psnr(img , filtered_img1)}')
    print(f'Average filter psnr with mask 5 = {psnr(img , filtered_img2)}')
    print(f'Average filter psnr with mask 7 = {psnr(img , filtered_img3)}')
    
    plt.show()
# Task-3(b) ends here

# ******************************************************************************* #
# Task-3(c) starts here
def task_3c():
    img = cv.resize(cv.imread('Images/shaun.jpg', cv.IMREAD_GRAYSCALE), (512, 512))

    noisy_img = np.copy(img)
    x=10000
    while x!=0:
        i = np.random.randint(0,512)
        j = np.random.randint(0,512)
        noisy_img[i,j] = 255
        x-=1
    x = 1e4
    while x!=0:
        i = np.random.randint(0,512)
        j = np.random.randint(0,512)
        noisy_img[i,j] = 0
        x-=1

    filtered_img1 = geometric_mean_filter(noisy_img, 5)
    filtered_img2 = harmonic_mean_filter(noisy_img, 5)

    plt.subplot(1,3,1)
    plt.imshow(filtered_img1, cmap='gray')
    plt.title('Geometric mean filter')

    plt.subplot(1,3,3)
    plt.imshow(filtered_img2, cmap='gray')
    plt.title('Harmonic mean filter')

    plt.subplot(1,3,2)
    plt.imshow(noisy_img, cmap='gray')
    plt.title('Noisy image')

    plt.tight_layout()
    plt.show()
    
    print(f'Geometric mean filter psnr with mask 5 = {psnr(img , filtered_img1)}')
    print(f'Harmonic mean filter psnr with mask 5 = {psnr(img , filtered_img2)}')

def main():
    # task_3a()
    # task_3b()
    task_3c()

if __name__=='__main__':
    main()