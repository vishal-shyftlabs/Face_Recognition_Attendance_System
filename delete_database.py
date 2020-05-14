import sqlite3
from tkinter import *
import os

conn = sqlite3.connect('database/database.db')
c = conn.cursor()

#taking input from user
root = Tk()
root.title("Deleting Database")

uid = Label(root, text="Enter Your Unique Registration Id: ")
uid_val = Entry(root)

uid.grid(row=0,rowspan=2,sticky=N+E+W+S)
uid_val.grid(row=0,rowspan=2,column=1,sticky=N+E+W+S)

def submit_e():
	global val1
	val1 = uid_val.get()
	root.destroy()

submit = Button(root, text="Submit",font=("times new roman",20),bg="brown",fg='white',command=submit_e)
submit.grid(row=2,columnspan=2,sticky=N+E+S+W)
root.mainloop()


c.execute("DELETE FROM students WHERE UID = ?",(str(val1),))
conn.commit()

# writing database in excel
os.system("python writing_in_excel.py")

for file in os.listdir('dataset/'):
	if (file.endswith('.jpg') and (str(val1) in file)) :
		os.remove('dataset/'+file)

conn.close()