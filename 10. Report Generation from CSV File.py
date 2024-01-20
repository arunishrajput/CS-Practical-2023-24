'''
Write a menu based program for following operations on a csv file:-
    1. Create a csv file 'employee.csv' with column header: - ID, Name, Address, Basic Pay.
    2. Insert the record in 'employee.csv' file
    3. Display the report of an employee based on ID. Report will contain
       the following information:
        ● Name of Employee:
        ● Total Credit:
        ● Basic Pay:
        ● DA:
        ● HRA:
        ● TPT:
        ● Total Debit:
        ● I-Tax:
        ● PF:
        ● Net Amount: Total Credit-Total Debit.
        (Hint: Calculate DA (20% of basic pay), HRA (10% of basic pay),
        TPT (3% of basic pay), PF (12% of basic Pay)
        ● I-Tax as per following criteria:
            ● If Total credit >50000, I-tax = 10% of total credit
            ● If Total credit >40000, I-tax = 5% of total credit
            ● If Total credit >30000, I-tax = 2% of total credit
            ● If Total credit <=30000, I-tax = NIL).
'''
#############################################################################

import csv, os

def make():
    with open('employees.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(['ID', 'Name', 'Address','Basic_pay'])

def create():
    if not os.path.exists('employees.csv'):
        make()
        print('File Created Successfully!')
    else:
        ch = (input('File already exists...Do you want to overwrite(Y/N)?')).upper()
        if ch == 'Y':
            make()
            print('File Overwritten Successfully!')

def write():
    if os.path.exists('employees.csv'):
        with open('employees.csv', 'a', newline='\n') as file:
            write  = csv.writer(file)
            ID = int(input('Enter Employee ID: '))
            name = input('Enter Employee Name: ')
            address = input('Enter Employee Address: ')
            basic_pay = int(input('Enter Employee Basic Pay: '))
            record = [ID, name, address, basic_pay]
            write.writerow(record)
            print('Record Inserted Successfully!')
    else:
        print('File not exists. First Create the File!')

def display():
    if os.path.exists('employees.csv'):
        with open('employees.csv', 'r', newline='\n') as file:
            read = csv.reader(file)
            next(read)
            id = int(input('Enter Employee ID to Search: '))
            found = 0
            for rec in read:
                if rec[0] == id:
                    BP = rec[3]
                    DA = 20*BP/100
                    HRA = 10*BP/100
                    TPT = 3*BP/100
                    PF = 12*BP/100
                    credit = BP+DA+HRA+TPT
                    if credit > 50000:
                        I_tax = 10*credit/100
                    elif credit > 40000:
                        I_tax = 5*credit/100
                    elif credit > 30000:
                        I_tax = 2*credit/100
                    elif credit <= 30000:
                        I_tax = 0
                    debit = PF+I_tax
                    net = credit - debit
                    print('Report of Employee ID', rec[0])
                    print('Name of Employee: ', rec[1])
                    print('Total Credit: ', credit)
                    print('Basic Pay: ', BP)
                    print('DA: ', DA)
                    print('HRA: ', HRA)
                    print('TPT: ', TPT)
                    print('Total Debit: ',debit)
                    print('Income Tax: ',I_tax)
                    print('PF: ',PF)
                    print('Net Amount: ',net)
                    found += 1
            if not found :
                print('Employee Not Found!')
    else:
        print('File not exists. First Create the File!')

while True:
    choice = int(input('''
1. Create File
2. Insert Records
3. display Report
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