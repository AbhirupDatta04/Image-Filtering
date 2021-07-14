
#Step 1
#Image Filtering using mean filter
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image,ImageFilter


img = cv2.imread('Eiffel.jpg') # reads the image
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV
fig_size = 9 
new_img = cv2.blur(img,(fig_size, fig_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_HSV2RGB)),plt.title('Using Mean filter')
plt.xticks([]), plt.yticks([])
plt.show() 


#Step 2
# The image will first be converted to grayscale and then filter
img2 = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
fig_size = 9
new_img = cv2.blur(img2,(fig_size, fig_size))
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(img2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_img, cmap='gray'),plt.title('Using Mean filter -Gray')
plt.xticks([]), plt.yticks([])
plt.show()


#Step 3
#Image Filtering using Gaussian Filter
new_img = cv2.GaussianBlur(img, (fig_size, fig_size),0)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_HSV2RGB)),plt.title('Using Gaussian Filter')
plt.xticks([]), plt.yticks([])
plt.show()



#Step 4
#grayscale Gaussian filtering
new_img_gauss = cv2.GaussianBlur(img2, (fig_size, fig_size),0)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(img2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_img_gauss, cmap='gray'),plt.title('Gaussian Filter-Gray')
plt.xticks([]), plt.yticks([])
plt.show()

#Step 5
#Median Filtering
new_img = cv2.medianBlur(img, fig_size)
plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(new_img, cv2.COLOR_HSV2RGB)),plt.title('Using Median Filter')
plt.xticks([]), plt.yticks([])
plt.show()

