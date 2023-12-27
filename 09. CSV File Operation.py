import csv
import os

def create():
    if not os.path.exists('student.csv'):
        with open('student.csv','w') as file:
            write = csv.writer(file)
            write.writerow(['Roll','Name','Address','Contact No.'])
        print('File created successfully!')
    else:
        print('File already exists!')

def write():
    if os.path.exists('student.csv'):
        with open('student.csv', 'a', newline='\n') as file:
            write  = csv.writer(file)
            roll = int(input('Enter roll number: '))
            name = input('Enter Student Name: ')
            address = input('Enter Student Address: ')
            contact = input('Enter Contact No.: ')
            record = [roll, name, address, contact]
            write.writerow(record)
            print('Record Inserted Successfully!')
    else:
        print('File not exists. First Create the File!')

def display():
    if os.path.exists('student.csv'):
        with open('student.csv', 'r', newline='\n') as file:
            read = csv.reader(file)
            next(read)
            count = 0
            for rec in read:
                print(rec)
                count += 1
            print('Total records: ', count)
    else:
        print('File not exists. First Create the File!')

while True:
    choice = int(input('''
1. Create File
2. Insert Records
3. display Records
0. Exit
Enter your choice:'''))
    if choice == 1:
        create()
    elif choice == 2:
        write()
    elif choice == 3:
        display()
    elif choice == 0:
        break
    else:
        print('Enter correct choice....')