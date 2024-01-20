'''
Write a menu based program for the following functionality in binary file 'markrec.dat':-
    1. Read name of student and his/her marks for five subjects, and write data in 'markrec.dat'.
    2. Display the report of any student based on name of student (input by user).
    Report will display following information:
        ● Name of student
        ● Marks obtained in five subjects (including name and marks of subjects)
        ● Total marks obtained
        ● Total percentage
        (Assume 500 is the maximum marks)
'''
#############################################################################

import pickle, os

def write():
    file = open('markrec.dat', 'ab')
    name = input('Enter name of the student: ')
    eng = int(input('Enter English marks: '))
    cs = int(input('Enter CS marks: '))
    phy = int(input('Enter Physics marks: '))
    chem = int(input('Enter Chemistry marks: '))
    math = int(input('Enter Mathematics marks: '))
    record = (name,eng,cs,phy,chem,math)
    pickle.dump(record,file)
    print('Record saved successfully!')
    file.close()

def display():
    if os.path.exists('markrec.dat'):
        file = open('markrec.dat', 'rb')
        name = input('Enter name of the student to search: ')
        try:
            while True:
                rec = pickle.load(file)
                if rec[0] == name:
                    total = rec[1]+rec[2]+rec[3]+rec[4]+rec[5]
                    percentage = total/5
                    print('Name of student:', rec[0])
                    print('Subject Marks:-')
                    print('English:', rec[1])
                    print('CS:', rec[2])
                    print('Physics:', rec[3])
                    print('Chemistry:', rec[4])
                    print('Mathematics:', rec[5])
                    print('Total Marks:', total)
                    print('Percentage:', percentage)
                    break
        except EOFError:
            print('Student not found!')
        file.close()
    else:
        print('markrec file not found!')

while True:
    choice = int(input('''
1. Enter New Record
2. Display Report of Student
0. Exit
Enter your choice:'''))
    if choice == 1:
        write()
    elif choice == 2:
        display()
    elif choice == 0:
        break
    else:
        print('Enter correct choice....')