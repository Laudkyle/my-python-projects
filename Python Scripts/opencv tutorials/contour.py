import cv2 as cv
import numpy as np

img = cv.imread('index.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
canny = cv.Canny(blurred, 125, 175)
blank = np.zeros(img.shape,"uint8")
# Thresholding
ret, thresh = cv.threshold(gray, 175, 255, cv.THRESH_BINARY)

# Identifying the contours
contours, heirachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours, -1, (0, 255, 225), thickness=1)


cv.imshow('Image', img)
cv.imshow('Blank', blank)
cv.imshow('Canny Image', canny)
cv.imshow('Threshold Image', thresh)
print(f'{len(contours)} contours were found in the image')

cv.waitKey(0)