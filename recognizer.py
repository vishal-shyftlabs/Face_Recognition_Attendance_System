import cv2
import os
import numpy as np
import time
import sys
import sqlite3 as sql

conn = sql.connect('database/database.db')
c = conn.cursor()

#flag for dismatch count
flag = 0
#recording the time of attendance
time_of_attendance = time.time()

#instance for cascade file
face_cas = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

#initializing camera for the time untill it records 30 images into dataset
cap_video = cv2.VideoCapture(0)

#creeating instance for LBPH algorithm
recognizer = cv2.face.LBPHFaceRecognizer_create()

#reading trainer.yml file 
recognizer.read('trainer/trainer.yml')

#selecting font
font = cv2.FONT_HERSHEY_SIMPLEX

#starting loop to recognize faces
while True:
	#ret is boolean variable to check if frame has been read correctly or not
	ret, img = cap_video.read()
	#converting color BGR to grayscale format
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#reading and scaling face from gray image using scale factor 1.3 and neighbor number =7
	faces = face_cas.detectMultiScale(gray, 1.3, 7)
	for (x,y,w,h) in faces:
		#extracting facial cordinates 
		roi_gray = gray[y:y+h,x:x+w]
		#creating a rectangle around the face
		cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0))
		#recognizer predicting the image after matching it and returning its id and confidence level
		id,conf = recognizer.predict(roi_gray)
		#putting text on rectangle around face 
		cv2.putText(img,str(id),(x,y-10),font,0.55,(120,255,120),1)
		if(conf<80):
			#marking present against that id
			for row in c.execute("SELECT * FROM students WHERE UID = ?",(str(id),)):
				if(str(id) == row[0]):
					c.execute("UPDATE students SET attendance= ? WHERE UID = ?",('Present',str(id)))
					conn.commit()
				else:
					os.system("python error_gui.py")
					flag = flag+1
					break
	
	cv2.imshow('frame',img)	
	#window opening time = 15seconds
	period = 15	
	if(flag == 10):
		os.system("python error_gui.py")
		break
	if(time.time()) > (time_of_attendance+period):
		break
	if(cv2.waitKey(100) & 0xFF == ord('q')):
		break

#writing attendance in excel
os.system("python Marking_attendance.py")

#closing the connection to sqlite3
conn.close()

cap_video.release();
cv2.destroyAllWindows();
