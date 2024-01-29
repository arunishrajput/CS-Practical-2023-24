'''
Write a menu-based program to perform the following operations on game table of Test database.
    1. Insert record through user set of values.
    2. Display the record of game table as per user choice of game.
    3. Modify the prizeMoney and scheduleDate for any game according to user choice.
    4. Delete a record of any gcode according to user choice.

Assume the following structure of game table:-
    +--------------------+-----------+------+
    | Field              | Data Type | Size |
    +--------------------+-----------+------+
    | Gcode(Primary Key) | INT       |  04  |
    | GameName           | VARCHAR   |  30  |
    | PrizeMoney         | FLOAT     |      |
    | ScheduleDate       | DATE      |      |
    +--------------------+-----------+------+
'''
#############################################################################

import mysql.connector as mc

def insert():
    cur = con.cursor()

    Gcode = int(input('Enter Game Code: '))
    GameName = input('Enter Game Name: ')
    PrizeMoney = float(input('Enter Prize Money: '))
    ScheduleDate = input('Enter Schedule Date: ')

    sql = f"INSERT INTO game VALUES ({Gcode}, '{GameName}', {PrizeMoney}, '{ScheduleDate}')"
    cur.execute(sql)
    con.commit()
    print('Record Inserted Successfully!')

    cur.close()

def display():
    cur = con.cursor()

    game = input('Enter Game Name to display record: ')

    sql = f"SELECT * FROM game WHERE GameName = '{game}'"
    cur.execute(sql)
    
    row = cur.fetchone()
    if row:
        print(row)
    else:
        print('Record Not Found!')

    cur.close()

def update():
    cur = con.cursor()

    game = input('Enter Game Name to update PrizeMoney and ScheduleDate: ')

    sql = f"SELECT * FROM game WHERE GameName = '{game}'"
    cur.execute(sql)

    if cur.fetchone():
        PrizeMoney = float(input('Enter new Prize Money: '))
        ScheduleDate = input('Enter new Schedule Date: ')
        sql = f"UPDATE game SET PrizeMoney = {PrizeMoney}, ScheduleDate = '{ScheduleDate}' WHERE GameName = '{game}'"
        cur.execute(sql)
        con.commit()
        print('PrizeMoney and ScheduleDate Updated Successfully!')
    else:
        print('Record not found!')

    cur.close()

def delete():
    cur = con.cursor()

    Gcode = int(input('Enter Game Code to delete its record: '))

    sql = f"SELECT * FROM game WHERE Gcode = {Gcode}"
    cur.execute(sql)

    if cur.fetchone():
        sql = f"DELETE FROM game WHERE Gcode = {Gcode}"
        cur.execute(sql)
        con.commit()
        print('Record Deleted Successfully!')
    else:
        print('Record not found!')

    cur.close()

con = mc.connect(host = 'localhost', user = 'root', password = 'password', database = 'Test')
while True:
    msg = '''1. Insert record into game
2. Display record
3. Update record
4. Delete record
0. Exit'''
    ch = int(input(f'{msg}\nEnter your choice: '))
    if ch == 1:
        insert()
    elif ch == 2:
        display()
    elif ch == 3:
        update()
    elif ch == 4:
        delete()
    elif ch == 0:
        break
    else:
        print('Invalid choice!')

con.close()
