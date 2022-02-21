import cv2
from tkinter import filedialog
import webbrowser
import matplotlib.pyplot as plt

config_file = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "frozen_inference_graph.pb"
model = cv2.dnn_DetectionModel(frozen_model, config_file)
classLabels =[]


file_name='Labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
    #classLabels.append(fpt.read())


model.setInputSize(320, 320)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputScale(1.0 / 127.5)
model.setInputSwapRB(True)

# # READING AN IMAGE
# img = cv2.imread('index.jpg')
# plt.imshow(img)
#
#
# img = cv2.imread('index.jpg')
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#
# classIndex, confidece, bbox = model.detect(img, confThreshold =0.5)
#
# print(classIndex)
# font_scale = 0.5
# font = cv2.FONT_HERSHEY_COMPLEX_SMALL
# for ClassInd, conf, boxes in zip(classIndex.flatten(), confidece.flatten(), bbox):
#     cv2.rectangle(img,boxes,(255,0,0),2)
#     cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40), font, fontScale = font_scale, color =(0,255,0),thickness = 1)
#
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
file_name=filedialog.askopenfilename()
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError('Cannot open video')

font_scale = 1
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

while True:
    ret, frame = cap.read()
    ClassIndex, confidece, bbox = model.detect(frame, confThreshold=0.55)

    print(ClassIndex)
    if (len(ClassIndex) != 0):
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
            if (ClassInd <= 80):
                cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font,
                            fontScale=font_scale, color=(0, 255, 0), thickness=1)

    cv2.imshow(file_name, frame)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


