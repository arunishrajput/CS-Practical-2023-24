'''
Write a python program to insert a record in student table of Test database through user set of values.

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

Roll = int(input('Enter Roll no.: '))
Name = input('Enter Name: ')
Address = input('Enter Address: ')
Phone = int(input('Enter Phone no.: '))

sql = f"INSERT INTO student VALUES ({Roll}, '{Name}', '{Address}', {Phone})"
cur.execute(sql)
con.commit()
print('Record Inserted Successfully!')

cur.close()
con.close()