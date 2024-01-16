def write():
    with open('employees.txt','a') as file:
        name = input('Enter name of the employee:')
        salary = input('Enter salary of the employee:')
        file.write(name+':'+salary+'\n')

def search():
    with open('employees.txt','r') as file:
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
    msg = '''1. Add employee
2. Show employee with salary in range 20000 - 30000
0. Exit'''
    choice = int(input(f"{msg}\nEnter your choice: "))
    if choice == 1:
        write()
    elif choice == 2:
        search()
    elif choice == 0:
        break
    else:
        print("Invalid choice. Try again.")