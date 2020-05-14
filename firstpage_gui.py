from tkinter import *
from datetime import datetime
import os

#creating the instance of tkinter window
root = Tk()

#configuring window background
root.configure(background="ivory4")

#providing tite for window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#main label 
label1 = Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),bg="red4",fg="white",height=2)
label1.grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#functions to call other python files
def c_dataset():
	os.system("python capture_database.py")

def write_e():
	os.system("python writing_in_excel.py")

def train_d():
	os.system("python training_dataset.py")

def m_attendance():
	os.system("python recognizer.py")

def v_attendance():
	os.startfile(os.getcwd()+"/Attendance_Files/attendance"+str(datetime.now().date())+'.xlsx')

def d_dataset():
	os.system("python delete_database.py")

def destroy():
    root.destroy()


#buttons and thier configuration
button1 = Button(root, text="Create Dataset",font=("times new roman",20),bg="dodgerblue2",fg='white',command=c_dataset)
button1.grid(row=2,rowspan=2,column=0,sticky=N+E+W+S,padx=10,pady=10)

button2 = Button(root, text="Write in Excel",font=("times new roman",20),bg="dodgerblue2",fg='white',command=write_e)
button2.grid(row=2,rowspan=2,column=1,sticky=N+E+W+S,padx=10,pady=10)

button3 = Button(root, text="Train Dataset",font=("times new roman",20),bg="dodgerblue3",fg='white',command=train_d)
button3.grid(row=4,rowspan=2,column=0,sticky=N+E+W+S,padx=10,pady=10)

button4 = Button(root, text="Mark Attendance",font=("times new roman",20),bg="dodgerblue3",fg='white',command=m_attendance)
button4.grid(row=4,rowspan=2,column=1,sticky=N+E+W+S,padx=10,pady=10)

button5 = Button(root, text="View Attendance Sheet",font=("times new roman",20),bg="dodgerblue4",fg='white',command=v_attendance)
button5.grid(row=6,rowspan=2,column=0,sticky=N+E+W+S,padx=10,pady=10)

button6 = Button(root, text="Delete Dataset",font=("times new roman",20),bg="dodgerblue4",fg='white',command=d_dataset)
button6.grid(row=6,rowspan=2,column=1,sticky=N+E+W+S,padx=10,pady=10)

button7 = Button(root,text="Exit",font=('times new roman',20),bg="red4",fg="white",command=destroy)
button7.grid(row=8,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#to keep window open for infinte time untill destroy() command is called
root.mainloop()