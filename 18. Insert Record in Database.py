import mysql.connector as mc

con = mc.connect(host = 'localhost', user = 'root', password = 'password', database = 'Test')

cur = con.cursor()

Roll = int(input('Enter Roll no.: '))
Name = input('Enter Name: ')
Address = input('Enter Address: ')
Phone = int(input('Enter Phone no.: '))

sql = f"INSERT INTO student VALUES ({Roll}, '{Name}', '{Address}', {Phone})"
print(sql)
cur.execute(sql)
con.commit()
print('Record Inserted Successfully!')

cur.close()
con.close()