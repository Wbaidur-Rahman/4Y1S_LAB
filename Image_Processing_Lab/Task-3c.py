# this program will calculate harmonic and geometric mean 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate PSNR
def psnr(original, noisy):
    mse = np.mean((original - noisy) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr_value

# Function to apply the geometric mean filter
def geometric_mean_filter(image, kernel_size):
    log_image = np.log(image + 1e-6)
    log_filtered = cv2.filter2D(log_image, -1, np.ones((kernel_size, kernel_size)))
    filtered = np.exp(log_filtered)
    return filtered


def harmonic_mean_filter(img, kernel_size):
    output = np.copy(img)
    h,w = img.shape
    
    for i in range (h):
        for j in range (w):
            a=0;d=0
            for k in range (i-3,i+3):
                for l in range (j-3,j+3):
                    if k<0 or k>=h or l<0 or l>=w: continue
                    
                    if(img[k][l]!=0):
                        a+=1/img[k][l]
                        d=d+1  
            output[i][j] = d/a; 
    return output
    

# def geometric(img):
#     return img

def main():
    img = cv2.imread('noisy_img.png',0)

    img = cv2.resize(img, [300,300])

    # noise = np.random.normal(0, 20, img.shape)
    # noisy_img = img + noise

    kernel_size = 3

    # img1 = geometric_mean_filter(noisy_img, kernel_size)
    img1 = geometric_mean_filter(img, kernel_size)
    plt.subplot(1,3,1)
    plt.imshow(img, cmap='gray')

    plt.subplot(1,3,2)
    plt.imshow(img1, cmap='gray')
    plt.show()

if __name__ == '__main__':
    main()