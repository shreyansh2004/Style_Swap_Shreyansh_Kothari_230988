import cv2
import matplotlib.pyplot as plt
import numpy as np


def gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size))
    k=(size-1)//2
    for i in range(size):
        for j in range(size):
            kernel[i, j] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(-((i - (k + 1)) ** 2 + (j - (k + 1)) ** 2) / (2 * sigma ** 2))
    return kernel

def convolution(image, kernel):
    #get dimensions
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    #initialize the convolved image
    convolved_image = np.zeros_like(image)

    #perform convolution
    for i in range(image_height + 1 - kernel_height):
        for j in range(image_width + 1 - kernel_width):
                convolved_image[i, j] = np.sum(image[i:i + kernel_height, j:j + kernel_width] * kernel[:,:])
    return convolved_image

#input image
image_path=input('Enter the path to the image: ')
image_path = image_path.replace('\\','\\\\').strip('"')
image = plt.imread(image_path)

#changing colour to gray
gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)



kernel = gaussian_kernel(3,3.0)
blured_image=convolution(gray_image,kernel)

#reLU 
blured_image = np.where(blured_image < 0, 0, blured_image)

#kernel for right vertical edge detection
l_kernel=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
#kernel for left vertical edge detection
r_kernel=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#kernel for top horizontal edge detection
t_kernel=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
#kernel for bottom horizontal edge detection
b_kernel=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])

#kernel for sobel operator
v_sober_kernel=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
h_sober_kernel=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

#kernel for Robert cross edge detection
robert_kernel_1=np.array([[1,0,0],[0,-1,0],[0,0,0]])
robert_kernel_2=np.array([[0,1,0],[-1,0,0],[0,0,0]])

#applying edge detection
l_edge_image=(convolution(blured_image,l_kernel))
r_edge_image=(convolution(blured_image,r_kernel))
t_edge_image=(convolution(blured_image,t_kernel))
b_edge_image=(convolution(blured_image,b_kernel))

v_sober=convolution(blured_image,v_sober_kernel)
h_sober=convolution(blured_image,h_sober_kernel)

robert_1=convolution(blured_image,robert_kernel_1)
robert_2=convolution(blured_image,robert_kernel_2)

plt.figure(figsize=(28,7))
plt.subplot(1,4,1)
plt.imshow(image, cmap='gray')
plt.title('original')

plt.subplot(1,4,2)
plt.imshow((r_edge_image**2 + l_edge_image**2 + t_edge_image**2 + b_edge_image**2)**(0.5), cmap='gray')
plt.title('edge detect with reLU')

plt.subplot(1,4,3)
plt.imshow((v_sober**2 + h_sober**2)**(0.5), cmap='gray')
plt.title('edge detect with sober operator')

plt.subplot(1,4,4)
plt.imshow((robert_1**2 + robert_2**2)**(0.5), cmap='gray')
plt.title('edge detect with Robert cross')


plt.show()



