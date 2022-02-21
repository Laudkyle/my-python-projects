import cv2 as cv
from tkinter import filedialog

# Reading images
# img = cv.imread('index.jpg')
# cv.imshow("Image", img)
# cv.waitKey(0)

# Rescaling
def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading Videos
capture = cv.VideoCapture(filedialog.askopenfilename())

while True:
    ret, frame = capture.read()
    frame_resized = rescale(frame)
    cv.imshow("Video", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
