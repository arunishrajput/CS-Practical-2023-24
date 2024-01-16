file = open('test.txt','r')
find = input('Enter word to find:')
content = file.read()

if find not in content.split():
    print('Find word', find, 'not found')
else:
    replace = input('Enter word to replace with:')
    replaced_content = content.replace(find,replace)
    with open('test.txt','w') as file:
        file.write(replaced_content)
        print('Replaced successfully!')
file.close()