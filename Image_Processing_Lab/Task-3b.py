import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image_path = 'shaun.jpg'

def psnr(original, noisy):
    mse = np.mean((original - noisy) ** 2)
    if mse == 0:
        return 100
    max_pixel = 255.0
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr_value
 
def average(img, order):
    output = np.copy(img)
    h,w = img.shape
 
    for i in range (h):
        for j in range (w):
            a=0;d=0
            for k in range (i-(order//2),i+((order+1)//2)):
                for l in range (j-(order//2),j+((order+1)//2)):
                    if k<0 or k>=h or l<0 or l>=w: continue
                    a+=img[k][l]
                    d+=1
            output[i][j] = a//d; 
    return output
 
def main():
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.resize(img, (512,512))

    noise = np.random.normal(0, 20, img.shape)
    noisy_img = img + noise

    plt.subplot(2,2,1)
    plt.imshow(noisy_img,cmap='gray')
    plt.title('Noisy Image')

    mask_order = 3
    img1 = average(noisy_img, mask_order)
    
    plt.subplot(2,2,2)
    plt.imshow(img1,cmap='gray')
    plt.title(f'Mask size : {mask_order}')

    psnr1 = psnr(img, img1)
    print(f"Average filter psnr (mask size = {mask_order}) : ",psnr1)

    mask_order = 5
    img1 = average(noisy_img, mask_order)
    
    plt.subplot(2,2,3)
    plt.imshow(img1,cmap='gray')
    plt.title(f'Mask size : {mask_order}')

    psnr1 = psnr(img, img1)
    print(f"Average filter psnr (mask size = {mask_order}) : ",psnr1)
 
    mask_order = 7
    img1 = average(noisy_img, mask_order)
    
    plt.subplot(2,2,4)
    plt.imshow(img1,cmap='gray')
    plt.title(f'Mask size : {mask_order}')

    psnr1 = psnr(img, img1)
    print(f"Average filter psnr (mask size = {mask_order}) : ",psnr1)
    plt.show()    
 
if __name__ == '__main__':
    main()
 
 