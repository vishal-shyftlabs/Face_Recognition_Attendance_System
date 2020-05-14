#pikesh was here

import sqlite3 as sql

con = sql.connect('database/database.db')
c = con.cursor()

'''
for row in c.execute("SELECT UID FROM students"):
	print(row)
	c.execute("UPDATE students SET attendance = ?",('Present',))
'''

#c.execute("UPDATE students SET attendance = ? WHERE UID =?",('No','11615139'))
c.execute("DROP TABLE students")
con.commit()

#for row in c.execute("SELECT * FROM students"):
#	print(row)

'''id  = 11615139

for row in c.execute("SELECT * FROM students WHERE UID = ?",(str(id),)):
	if(str(id) == row[0]):
		print(row)
	else:
		print("1. record doesn't exist")

if(str(id) == c.execute("SELECT UID FROM students WHERE UID = ?",(str(id),))):
	for row in c.execute("SELECT * FROM students WHERE UID = ?",(str(id),)):
		print(row)
else:
	print("2. record doesn't exist")

#c.execute("UPDATE students SET attendance= ? WHERE UID = ?",('Yes',str(id)))

for row in c.execute("SELECT * FROM students WHERE UID = ?",(str(id),)):
	print(row)
'''
con.close()

'''
IF EXISTS (SELECT * FROM Products WHERE id = ?)
BEGIN
--do what you need if exists
END
ELSE
BEGIN
--do what needs to be done if not
END
'''