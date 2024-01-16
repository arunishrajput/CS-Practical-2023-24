file = open('story.txt', 'r')
line = file.readline().lower()
a = an = the = 0
while line:
    for word in line.split():
        if word == 'a':
            a += 1
        elif word == 'an':
            an += 1
        elif word == 'the':
            the += 1
    line = file.readline().lower()
print('Total no. of a:',a)
print('Total no. of an:',an)
print('Total no. of the:',the)
file.close()