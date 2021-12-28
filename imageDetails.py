import cv2
img = cv2.imread('rose.png')
print('Image Properties')
print('Number of pixels ' + str(img.size))
print('Shape/Dimensions ' + str(img.shape))

'''Splitting an Image into Individual Channels'''
from google.colab.patches import cv2_imshow

blue, green, red = cv2.split(img)
img_gs = cv2.imread('rose.png',cv2.IMREAD_GRAYSCALE)

cv2_imshow(red)
cv2_imshow(blue)
cv2_imshow(green)
cv2_imshow(img_gs)
