import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image_path = 'shaun.jpg'
 
def average(img):
    output = np.copy(img)
    h,w = img.shape
 
    for i in range (h):
        for j in range (w):
            a=0;d=0
            for k in range (i-2,i+3):
                for l in range (j-2,j+3):
                    if k<0 or k>=h or l<0 or l>=w: continue
                    d+=1
                    a+=img[k][l]
 
            output[i][j] = a//d; 
    return output
 
def main():
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (512,512))
    img = average(img)
 
    noise = np.random.normal(0, 20, img.shape)
    noisy_img = img + noise
    img = average(noisy_img)
 
    plt.subplot(2,1,1)
    plt.imshow(noisy_img,cmap='gray')
    plt.title('Noisy Image')
    plt.subplot(2,1,2)
    plt.imshow(img,cmap='gray')
    plt.title('Filtered Image')
 
    plt.show()    
 
if __name__ == '__main__':
    main()
 
 