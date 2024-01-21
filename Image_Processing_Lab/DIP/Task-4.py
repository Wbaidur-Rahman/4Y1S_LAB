import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def butterworth_lowpass_filter(freq_img, n, cutoff):
    h,w = freq_img.shape
    butterworth_filter = np.zeros(freq_img.shape, dtype= np.float32)

    for u in range (h):
        for v in range (w):
            D = np.sqrt((h/2-u)**2+(w/2-v)**2)
            butterworth_filter[u,v] = 1/(1+D/cutoff)**(2*n)
    
    filtered_img = np.fft.ifft2(np.fft.fftshift(freq_img*butterworth_filter))
    return np.abs(filtered_img)


def gaussian_lowpass_filter(freq_img, cutoff):
    h,w = freq_img.shape
    filter = np.zeros(freq_img.shape, dtype= np.float32)

    for u in range (h):
        for v in range (w):
            D = np.sqrt((h/2-u)**2+(w/2-v)**2)
            filter[u,v] = np.exp(-(D**2)/(2*(cutoff**2)))

    filtered_img = np.fft.ifft2(np.fft.fftshift(freq_img*filter))
    return np.abs(filtered_img)


def ideal_lowpass_filter(freq_img, cutoff):
    h,w = freq_img.shape
    filter = np.zeros(freq_img.shape, dtype= np.float32)

    for u in range (h):
        for v in range (w):
            D = np.sqrt((h/2-u)**2+(w/2-v)**2)
            filter[u,v] = 1*(D<=cutoff)
    
    filtered_img = np.fft.ifft2(np.fft.fftshift(freq_img*filter))
    return np.abs(filtered_img)


def ideal_highpass_filter(freq_img, cutoff):
    h,w = freq_img.shape
    filter = np.zeros(freq_img.shape, dtype= np.float32)

    for u in range (h):
        for v in range (w):
            D = np.sqrt((h/2-u)**2+(w/2-v)**2)
            filter[u,v] = 1*(D>=cutoff)
    
    filtered_img = np.fft.ifft2(np.fft.fftshift(freq_img*filter))
    return np.abs(filtered_img)


def gaussian_highpass_filter(freq_img, cutoff):
    h,w = freq_img.shape
    filter = np.zeros(freq_img.shape, dtype= np.float32)

    for u in range (h):
        for v in range (w):
            D = np.sqrt((h/2-u)**2+(w/2-v)**2)
            filter[u,v] = 1-np.exp(-(D**2)/(2*(cutoff**2)))

    filtered_img = np.fft.ifft2(np.fft.fftshift(freq_img*filter))
    return np.abs(filtered_img)


# ******************************************************
# *****************************
# ***************

def task_4a(noisy_img, freq_img):
    guassian_filtered_img = gaussian_lowpass_filter(freq_img, 25)
    butterworth_filtered_img = butterworth_lowpass_filter(freq_img, 2, 25)

    plt.subplot(1,3,1)
    # plt.imshow(np.log(np.abs(freq_img)), cmap=  'gray')
    plt.imshow(noisy_img, cmap='gray')
    plt.title('Alphabet')

    plt.subplot(1,3,2)
    plt.imshow(guassian_filtered_img, cmap='gray')
    plt.title('Gaussian Filtered Image')

    plt.subplot(1,3,3)
    plt.imshow(butterworth_filtered_img, cmap='gray')
    plt.title('Butterworth Filtered Image')

# task 4_B starts here ########################################################
# *
# *
# ################################**********************************************


def task_4b(noisy_img, freq_img):
    plt.subplot(2,3,1)
    # plt.imshow(np.log(np.abs(freq_img)), cmap=  'gray')
    plt.imshow(noisy_img, cmap='gray')
    plt.title('Noisy Alphabet')

    for i in range (5):
        Ideal_filtered_img = ideal_lowpass_filter(freq_img, (i+1)*5)
        plt.subplot(2,3,i+2)
        plt.imshow(Ideal_filtered_img, cmap='gray')
        plt.title(f'Ideal Filtered Image with cutoff {(i+1)*5}')

# ****************************************************************************************** #

def task_4c(noisy_img, freq_img):
    plt.subplot(2,3,1)
    # plt.imshow(np.log(np.abs(freq_img)), cmap=  'gray')
    plt.imshow(noisy_img, cmap='gray')
    plt.title('Noisy Alphabet')

    for i in range (2):
        Ideal_filtered_img = ideal_highpass_filter(freq_img, (i+1)*10)
        plt.subplot(2,3,i+2)
        plt.imshow(Ideal_filtered_img, cmap='gray')
        plt.title(f'Ideal Filtered Image with cutoff {(i+1)*10}')

    for i in range (3):
        gaussian_filtered_img = gaussian_highpass_filter(freq_img, (i+1)*10)
        plt.subplot(2,3,i+4)
        plt.imshow(gaussian_filtered_img, cmap='gray')
        plt.title(f'Gaussian Filtered Image with cutoff {(i+1)*10}')


def main():
    img = cv.resize(cv.imread('Images/alphabet.png', cv.IMREAD_GRAYSCALE), (512,512))
    gaussian_noise = np.random.normal(7, 13, img.shape).astype(np.uint8)
    noisy_img = cv.add(img, gaussian_noise)
    freq_img = np.fft.fftshift(np.fft.fft2(img))

    # task_4a(noisy_img=noisy_img, freq_img=freq_img)
    # task_4b(noisy_img=noisy_img, freq_img=freq_img)
    task_4c(noisy_img=noisy_img, freq_img=freq_img)

    plt.tight_layout()
    plt.show()

if __name__=='__main__':
    main()