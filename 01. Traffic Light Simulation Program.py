def traficlight():
    
    code = light(input('Enter the status of light: ').upper())
    
    if code == 0:
        print('STOP, your life is precious')
    elif code == 1:
        print('Please WAIT till light is green')
    elif code == 2:
        print('GO! Thanks for being patient')
    elif code == 3:
        print('Enter Valid Colour')


def light(status):
    if status == 'RED':
        return 0
    elif status == 'YELLOW':
        return 1
    elif status == 'GREEN':
        return 2
    else:
        return 3
    
traficlight()
print('SPEED THRILLS BUT KILLS')