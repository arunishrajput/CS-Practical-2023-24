def trafficlight():
    
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
    return {'RED': 0, 'YELLOW': 1, 'GREEN': 2}.get(status, 3)

    
trafficlight()
print('SPEED THRILLS BUT KILLS')

hello