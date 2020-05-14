from tkinter import *

root = Tk()
root.title("Message")
root.geometry("300x100")
message = Label(root, text="Successfully Done! :)")
message.configure(bg="green",fg="white",height=3)
message.pack(side='top')

def submit_e():
	root.destroy()

submit = Button(root, text="Message Recieved",font=("times new roman",20),bg="brown",fg='white',command=submit_e)
submit.pack(side='bottom')

root.mainloop()