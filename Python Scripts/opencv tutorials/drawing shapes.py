import cv2 as cv
import numpy as np

# Creating a blank image
blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)
#
#
# # Painting a different color
# blank[:] = 0, 255, 0
# cv.imshow("Green", blank)


# drawing in the color[range of height : range of width]
blank[200:300, 200:300] = 123, 110, 232
# Drawing a rectangle
cv.rectangle(blank, (150, 150), (350, 350), (0, 255, 0), thickness=3)
# Drawing a circle
cv.circle(blank, (250, 250), 50, (0, 0, 235), thickness=3)
# Drawing a line
cv.line(blank,(150, 250), (350,250),(255, 0, 0), thickness=3)
cv.line(blank,(250, 150), (250,350),(255, 0, 0), thickness=3)
# Writing text onto an image
cv.putText(blank,"Hello Drawings", (50, 100), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2.0, (0, 255, 255), thickness=3)
cv.imshow("Drawing", blank)
cv.waitKey(0)

