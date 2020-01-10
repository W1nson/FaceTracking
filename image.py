import cv2
import numpy as np 

face_cascade = cv2.CascadeClassifier('/Users/winsonchen/anaconda3/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('/Users/winsonchen/anaconda3/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')

print(face_cascade)
print(eye_cascade)


cap = cv2.VideoCapture(0)
ret, frame = cap.read()

windowWidth=frame.shape[1]
windowHeight=frame.shape[0]
print(windowWidth, windowHeight)
print()
last = 640
while True: 
	ret, img = cap.read() 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces: 
		cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
		print('x:',x, windowWidth-(x+w))
		print(w)
		print('y:',y, windowHeight-(y+h))
		print(h)
                #1280 x 720
		#center (640,360)
		print('move joystick:', x - last)
		last = x
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in eyes: 
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255, 0), 2)

	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff 
	if k == 27: 
		break 

cap.release()
cv2.destroyAllWindows()

