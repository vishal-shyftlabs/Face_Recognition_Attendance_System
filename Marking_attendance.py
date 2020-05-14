import sqlite3 as sql
import win32com.client as win32
import os
from datetime import datetime

if os.path.exists('/Attendance_Files/Attendance'+str(datetime.now().date())+'.xlsx'):
	os.remove('/Attendance_Files/Attendance'+str(datetime.now().date())+'.xlsx')

conn = sql.connect('database/database.db')
c = conn.cursor()

#create out instance of excel
excelApp = win32.gencache.EnsureDispatch("Excel.Application")

#get the workbook
if not os.path.exists('Attendance_Files/'+'Attendance'+str(datetime.now().date())+'.xlsx'):
	if not os.path.exists('Attendance_Files'):
		os.makedirs("Attendance_Files")
	ExcelWrkbook = excelApp.Workbooks.Add()
	ExcelWrkbook.SaveAs(os.getcwd()+'/Attendance_Files/Attendance'+str(datetime.now().date())+'.xlsx')
else:
	bookname = str(os.getcwd()+'/Attendance_Files/Attendance'+ str(datetime.now().date())+'.xlsx')
	ExcelWrkbook = excelApp.Workbooks.Open(os.getcwd()+'/Attendance_Files/Attendance'+ str(datetime.now().date())+'.xlsx')

#get the worksheet
Excelwrksheet = ExcelWrkbook.ActiveSheet

#get xl constants
xlRight = win32.constants.xlToRight
xlDown = win32.constants.xlDown

def get_data():
	c.execute("SELECT * FROM students ORDER BY student_name")
	return c.fetchall()

students = get_data()

#creating the header
firstheaderCell = Excelwrksheet.Cells(1,1)
lastheaderCell = Excelwrksheet.Cells(1,3)
ExcelHeaderRange = Excelwrksheet.Range(firstheaderCell, lastheaderCell)
ExcelHeaderRange.Value = ('UID', 'Name', 'Attendance')

# get the length of a row
RowLength = len(students[0])
#print(RowLength)

#get the length of a column
ColLength = len(students)
#print(ColLength)

#define the first and last cell in out range
FirstCell = Excelwrksheet.Cells(2,1)
LastCell = Excelwrksheet.Cells(1+ColLength,RowLength)

#get the range
ExcelRange = Excelwrksheet.Range(FirstCell, LastCell)
ExcelRange.Value = students

#close and save the workbook
ExcelWrkbook.Close(True)

#####testing bachi hai####
for row in c.execute("SELECT * FROM students"):
	c.execute("UPDATE students SET attendance = ?",('Absent',))
	conn.commit()

os.system("python message_gui.py")

conn.close()