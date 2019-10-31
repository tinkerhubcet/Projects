import cv2
cap = cv2.VideoCapture(0)
count = 1
while(True):
    ret, frame = cap.read()
    cv2.imwrite("training-data\s1\Image"+str(count)+".jpg",frame)
    cv2.imshow("frame",frame)
    count=count+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if count >=30:
        break
cap.release()
