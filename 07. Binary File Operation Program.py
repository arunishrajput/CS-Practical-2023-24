import pickle, os

def write():
    file = open('stock.dat','ab')
    ID = int(input('Enter Product ID: '))
    Name = input('Enter Product Name: ')
    Qty = int(input('Enter Product Quantity: '))
    Price = int(input('Enter Product Price: '))
    record = {'ID':ID, 'Name':Name, 'Quantity':Qty, 'Price':Price}
    pickle.dump(record, file)
    print('Record saved successfully!')
    file.close()

def display():
    if os.path.exists('stock.dat'):
        file = open('stock.dat','rb')
        count = 0
        try:
            while True:
                record = pickle.load(file)
                print(record)
                count += 1
        except EOFError:
            print('Total record:',count)
        file.close()
    else:
        print('Stock file not found!')

def search():
    if os.path.exists('stock.dat'):
        file = open('stock.dat','rb')
        ID = int(input('Enter product ID to search: '))
        try:
            while True:
                record = pickle.load(file)
                if record['ID'] == ID:
                    print(record)
                    break
        except EOFError:
            print('Record not found!')
        file.close()
    else:
        print('Stock file not found!')

def modify():
    if os.path.exists('stock.dat'):
        file = open('stock.dat','rb')
        newfile = open('newstock.dat','wb')
        ID = int(input('Enter product ID to modify: '))
        found = 0
        try:
            while True:
                record = pickle.load(file)
                if record['ID'] == ID:
                    found = 1
                    print('Modify -->',record)
                    Name = input('Enter New Product Name: ')
                    Qty = int(input('Enter New Product Quantity: '))
                    Price = int(input('Enter New Product Price: '))
                    record = {'ID':ID, 'Name':Name, 'Quantity':Qty, 'Price':Price}
                    pickle.dump(record,newfile)
                else:
                    pickle.dump(record,newfile)
        except EOFError:
            if found:
                print('Record Modified Successfully!')
            else:
                print('Record Not Found!')
        file.close()
        newfile.close()
        os.remove('stock.dat')
        os.rename('newstock.dat','stock.dat')
    else:
        print('File not found!')

def delete():
    if os.path.exists('stock.dat'):
        file = open('stock.dat','rb')
        newfile = open('newstock.dat','wb')
        ID = int(input('Enter ID to delete: '))
        found = 0
        try:
            while True:
                record  = pickle.load(file)
                if record['ID'] == ID:
                    found = 1
                else:
                    pickle.dump(record, newfile)
        except EOFError:
            if found:
                print('Record deleted successfully!')
            else:
                print('Record not found!')
        file.close()
        newfile.close()
        os.remove('stock.dat')
        os.rename('newstock.dat','stock.dat')
    else:
        print('File Not Found!')

while True:
    msg = '''1. Enter stock
2. Display stock
3. Search Product
4. Modify Product
5. Delete Product
0. Exit'''
    choice = int(input(f"{msg}\nEnter your choice:"))
    if choice == 1:
        write()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        modify()
    elif choice == 5:
        delete()
    elif choice == 0:
        break
    else:
        print('Enter correct choice....')