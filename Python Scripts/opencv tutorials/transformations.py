import cv2 as cv
import numpy as np

img = cv.imread("index1.jpg")

# Translating Images
def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimension)

"""
+x = right
-x = left
+y = down
-y = up
"""
# Rotating an image

def rotate(img, angle, rotPoint = None):
    (width, height) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rotMat, dimension)

# Flipping an image
flip = cv.flip(img, 1)
"""
0 = vertical
1 = horizontal
-1 = both
"""

rotated = rotate(img, 150)
translated = translate(img, -50, 50)


cv.imshow('Image', img)
cv.imshow('Flipped Image', flip)
cv.imshow('Translated Image', translated)
cv.imshow('Rotated Image', rotated)
cv.waitKey(0)