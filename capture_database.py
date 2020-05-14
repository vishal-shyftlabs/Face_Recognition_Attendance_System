import sqlite3
import cv2
import os
from tkinter import *


#taking input from user
root = Tk()
root.title("Creating Database")

uid = Label(root, text="Enter Your Unique Registration Id: ")
name = Label(root, text="Enter Your Full Name: ")
uid_val = Entry(root)
name_val = Entry(root)

uid.grid(row=0,rowspan=2,sticky=N+E+W+S)
uid_val.grid(row=0,rowspan=2,column=1,sticky=N+E+W+S)

name.grid(row=2,rowspan=2,sticky=E)
name_val.grid(row=2,rowspan=2,column=1,sticky=N+E+W+S)

def submit_e():
	global val1,val2
	val1 = uid_val.get()
	val2 = name_val.get()
	root.destroy()

submit = Button(root, text="Submit",font=("times new roman",20),bg="brown",fg='white',command=submit_e)
submit.grid(row=4,columnspan=2,sticky=N+E+S+W)
root.mainloop()


dir1 = os.path.dirname("database/database.db")
if not os.path.exists(dir1):
	os.makedirs("database")
	os.system("python sql.py")

conn = sqlite3.connect('database/database.db')
c = conn.cursor()

def assure_path_exists(path):
	dir = os.path.dirname(path)
	if not os.path.exists(dir):
		os.makedirs(dir)


face_id = str(val1)
name = str(val2)

c.execute("INSERT INTO students(UID,student_name,attendance) VALUES(?,?,?)",(face_id,name,'Absent'))
conn.commit()

#start capturing Video
vid_cam = cv2.VideoCapture(0)

#detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

#initaializing count variabe to count scanned images
count  = 0
assure_path_exists("dataset/")

#start scanning loop
while(True):
	#capture video frame
	_,image_frame = vid_cam.read()
	cv2.imshow('frame',image_frame)

	#convert frame to grayscale
	gray = cv2.cvtColor(image_frame,cv2.COLOR_BGR2GRAY)

	#detect frames of different sizes, list of faces rectangles
	faces = face_detector.detectMultiScale(gray,1.3,5)

	# Loops for each face
	for(x,y,w,h) in faces:
		#crop the image frame into rectangle
		cv2.rectangle(image_frame,(x,y),(x+w,y+h),(255,0,0),2)
		#increment count
		count += 1

		#save the captured image into datasets folder
		cv2.imwrite("dataset/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])

		#display the video frame, with bounded rectangle on image frame
		cv2.imshow('frame',image_frame)
	
	#to stop scanning images, press 'q' for at least 100ms
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
	elif count>=30:
		os.system("python message_gui.py")
		break

#stop video
vid_cam.release()

#CLOSE all started windows
cv2.destroyAllWindows()

conn.close()