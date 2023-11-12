import cv2
import numpy as np
import matplotlib.pyplot as plt


def erosion(img, se):
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

    rows, columns = img.shape
    output_img = np.zeros((rows, columns), dtype=np.uint8)

    for i in range(0, rows-se.shape[0]):
        for j in range(0, columns-se.shape[1]):
            cut_img = img[i:i + se.shape[0], j:j + se.shape[1]]
            nh_img = (cut_img * se)
            output_img[i, j] = np.min(nh_img)

    return output_img

def dilation(img, se):
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

    rows, columns = img.shape
    output_img = np.zeros((rows, columns), dtype=np.uint8)

    for i in range(0, rows-se.shape[0]):
        for j in range(0, columns-se.shape[1]):
            cut_img = img[i:i + se.shape[0], j:j + se.shape[1]]
            nh_img =  (cut_img * se)
            output_img[i, j] = np.max(nh_img)

    return output_img

def Task_5a():
    # Load image
    img = cv2.imread('im.png', cv2.IMREAD_GRAYSCALE)

    # Structuring element
    se = np.ones((3,3), dtype=np.uint8)


    # Erosion and Dilation
    eroded_img = erosion(img, se)
    dilated_img = dilation(img, se)

    # Display results
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1], cmap='gray')
    plt.title('Before Erosion')

    plt.subplot(2, 2, 2)
    plt.imshow(eroded_img, cmap='gray')
    plt.title('After Erosion')

    plt.subplot(2, 2, 3)
    plt.imshow(dilated_img, cmap='gray')
    plt.title('After Dilation')

def Task_5b():
    # Load image
    img = cv2.imread('fingerprint.png', cv2.IMREAD_GRAYSCALE)

    # Structuring element
    se = np.ones((5,5), dtype=np.uint8)

    # cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]


    # Erosion and Dilation
    erosion_img = erosion(img, se)
    opening = dilation(erosion_img, se)

    dilation_img = dilation(opening, se)
    closing = erosion(dilation_img, se)

    # Display results
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1], cmap='gray')
    plt.title('Before Erosion')

    plt.subplot(2, 2, 2)
    plt.imshow(opening, cmap='gray')
    plt.title('After Opening')

    plt.subplot(2, 2, 3)
    plt.imshow(closing, cmap='gray')
    plt.title('After Closing')

def Task_5c():
    # Load image
    img = cv2.imread('boundary.png', cv2.IMREAD_GRAYSCALE)

    # Structuring element
    se = np.ones((10,10), dtype=np.uint8)

    # Erosion and Dilation
    erosion_img = erosion(img, se)
    boundary = img-erosion_img

    # Display results
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.imshow(cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1], cmap='gray')
    plt.title('Original image')

    plt.subplot(2, 1, 2)
    plt.imshow(boundary, cmap='gray')
    plt.title('The boundary')


def main():
    # Task_5a()
    # Task_5b()
    Task_5c()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()