# this program will calculate harmonic and geometric mean 

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('shaun.jpg', 0)

def harmonic(img):
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
    

def geometric(img):
    return img

def main():
    img = cv2.imread('shaun.jpg',0)
    # img = cv2.resize(img, [10,10])

    img1 = harmonic(img)
    plt.imshow(img1, cmap='gray')
    plt.show()

if __name__ == '__main__':
    main()