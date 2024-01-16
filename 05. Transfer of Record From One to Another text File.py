readfile = open('employee.txt','r')
writefile = open('emp.txt','w')

count = 0
line = readfile.readline()
while line:
    salary = int(line.split(':')[1])
    if salary > 25000:
        writefile.write(line)
        count += 1
    line = readfile.readline()
readfile.close()
writefile.close()
print('Total no. of records added: ',count)