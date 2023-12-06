file = open('test.txt', 'r')
content = file.read().lower()
a = an = the = 0
for word in content.split():
    if word == 'a':
        a += 1
    elif word == 'an':
        an += 1
    elif word == 'the':
        the += 1
print('Total no. of a:',a)
print('Total no. of an:',an)
print('Total no. of the:',the)
file.close()