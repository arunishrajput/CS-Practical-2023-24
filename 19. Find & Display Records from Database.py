'''
Write a python program to find and display the record of student from student table of Test database.
Program will search the record by the input roll no. of student. If record not found, then display appropriate message.

Assume the following structure of student table:-
    +-------------------+-----------+------+
    | Field             | Data Type | Size |
    +-------------------+-----------+------+
    | Roll(Primary Key) | INT       |  04  |
    | Name              | VARCHAR   |  30  |
    | Address           | CHAR      |  40  |
    | Phone_no          | VARCHAR   |      |
    +-------------------+-----------+------+
'''
#############################################################################

import mysql.connector as mc

con = mc.connect(host = 'localhost', user = 'root', password = 'password', database = 'Test')

cur = con.cursor()

Roll = int(input('Enter Roll no. to display record: '))

sql = f"SELECT * FROM student WHERE Roll = {Roll}"
cur.execute(sql)

row = cur.fetchone()
if row:
    print(row)
else:
    print('No records found!')

cur.close()
con.close()