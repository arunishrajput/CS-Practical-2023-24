file = open('employees.txt','a+')

def write():
    name = input('Enter name of the employee:')
    salary = input('Enter salary of the employee:')
    file.write(name+':'+salary+'\n')

def read():
    file.seek(0)
    line = file.readline()
    if line:
        while line:
            salary = int(line.split(':')[1])
            if salary >= 20000 and salary <= 30000:
                print('employee with salary in range 20000 - 30000-->',line)
            line = file.readline()
        else:
            print('No employee has salary in range 20000 - 30000')
    else:
        print('No data found!')

while True:
    choice = int(input('''1. Add employee
2. Show employee with salary in range 20000 - 30000
3. Exit
Enter your choice: '''))
    if choice == 1:
        write()
    elif choice == 2:
        read()
    elif choice == 3:
        break
file.close()