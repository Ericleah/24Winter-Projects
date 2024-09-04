import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    success, img = cap.read()


    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff == ord('q') or cv2.getWindowProperty('Image',cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()