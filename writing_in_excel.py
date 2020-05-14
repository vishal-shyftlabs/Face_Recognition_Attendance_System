import sqlite3 as sql
import win32com.client as win32
import os

if os.path.exists('database/Students_Database_Sheet.xlsx'):
	os.remove('database/Students_Database_Sheet.xlsx')

conn = sql.connect('database/database.db')
c = conn.cursor()

#create out instance of excel
excelApp = win32.gencache.EnsureDispatch("Excel.Application")


#get the workbook
if not os.path.exists('database/Students_Database_Sheet.xlsx'):
	if not os.path.exists('database'):
		os.makedirs("database")
	ExcelWrkbook = excelApp.Workbooks.Add()
	ExcelWrkbook.SaveAs(os.getcwd()+'/database/Students_Database_Sheet.xlsx')
else:
	bookname = str(os.getcwd()+'/database/Students_Database_Sheet.xlsx')
	ExcelWrkbook = excelApp.Workbooks.Open(bookname)

#get the worksheet
Excelwrksheet = ExcelWrkbook.ActiveSheet


def get_data():
	c.execute("SELECT * FROM students ORDER BY UID")
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

os.system("python message_gui.py")

conn.close()

os.startfile(os.getcwd()+'/database/Students_Database_Sheet.xlsx')