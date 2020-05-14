import sqlite3

#establishing a connection with database
conn = sqlite3.connect('database/database.db')
c = conn.cursor()

#creating a table named students in database to record students credentials
c.execute("CREATE TABLE students (UID text,student_name text, attendance text)")

#saving the changes in database
conn.commit()

#closing the connection
conn.close()