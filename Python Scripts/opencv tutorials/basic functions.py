import cv2 as cv

img = cv.imread("index.jpg")
# Converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Blurring the image
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# Creating an Edge cascade
canny = cv.Canny(img, 125, 175)
# Dilating Image
dilated = cv.dilate(canny, (3, 3), iterations=1)
# Eroding an image (Getting back the edges of a dilated image)
erode = cv.erode(dilated,(3, 3), iterations=1)
# resizing an image
resized = cv.resize(img, (400, 400), interpolation=cv.INTER_CUBIC)
# Cropping an image
cropped = resized[50:150, 250:400]

cv.imshow('Cropped Image', cropped)
cv.imshow("Resized Image", resized)
cv.imshow("Eroded Image", erode)
cv.imshow("Dilated Image", dilated)
cv.imshow("Blur Image", blur)
cv.imshow("Canny Image", canny)
cv.imshow("Image", gray)
cv.waitKey(0)
