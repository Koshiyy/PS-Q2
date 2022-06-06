import cv2 as cv
import numpy as np

cap = cv.VideoCapture('./assets/images/q2.mp4')

if (cap.isOpened() == False):
    print('Error opening video file')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        upper_red = np.array([180, 255, 255])
        lower_red = np.array([160, 50, 50])
        mask_red1 = cv.inRange(frame_hsv, lower_red, upper_red)

        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask_red2 = cv.inRange(frame_hsv, lower_red, upper_red)

        mask_red = mask_red1 + mask_red2

        cnts = cv.findContours(mask_red, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        lower_black = np.array([0, 0, 0])
        upper_black = np.array([5, 200, 200])
        mask_black = cv.inRange(frame_hsv, lower_black, upper_black)

        cnts2 = cv.findContours(mask_black, cv.RETR_TREE,
                                cv.CHAIN_APPROX_SIMPLE)
        cnts2 = cnts2[0] if len(cnts2) == 2 else cnts2[1]

        vermelho = 0

        for c2 in cnts2:
            x2, y2, w2, h2 = cv.boundingRect(c2)
            area2 = cv.contourArea(c2)
            if(area2 > 5000):
                rect = cv.rectangle(
                    frame, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 3)
                for c in cnts:
                    x, y, w, h = cv.boundingRect(c)
                    area = cv.contourArea(c)
                    if(area > 1500):
                        vermelho += 1
                        print(vermelho)
                        rect = cv.rectangle(
                            frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv.imshow('Frame', frame)

        if cv.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
