'''
Write a python program to update the address of student in student table of Test database.
Program will search the record by the input roll no. of student. If record not found,
then display appropriate message.

Assume the following structure of student table:-
    +-------------------+-----------+------+
    | Field             | Data Type | Size |
    +-------------------+-----------+------+
    | Roll(Primary Key) | INT       |  04  |
    | Name              | VARCHAR   |  30  |
    | Address           | CHAR      |  40  |
    | Phone_no          | INT       |      |
    +-------------------+-----------+------+
'''
#############################################################################

import mysql.connector as mc

con = mc.connect(host = 'localhost', user = 'root', password = 'password', database = 'Test')
cur = con.cursor()

Roll = int(input('Enter Roll no. to update address: '))

sql = f"SELECT * FROM student WHERE Roll = {Roll}"
cur.execute(sql)

if cur.fetchone():
    address = input('Enter new address: ')
    sql = f"UPDATE student SET Address = '{address}' WHERE Roll = {Roll}"
    cur.execute(sql)
    con.commit()
    print('Address Updated Successfully!')
else:
    print('Record not found!')

cur.close()
con.close()
