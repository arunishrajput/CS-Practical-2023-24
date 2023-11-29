file = open('test.txt','r+')
find = input('Enter word to find:')
content = file.read()

if find not in content:
    print('Find word', find, 'not found')
    file.close()
else:
    replace = input('Enter word to replace with:')
    replaced_content = content.replace(find,replace)
    file.seek(0)
    file.write(replaced_content)
    print('Replaced successfully!')
file.close()