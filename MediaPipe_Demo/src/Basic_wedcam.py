import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    cv2.imshow("Image", img)
	
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()