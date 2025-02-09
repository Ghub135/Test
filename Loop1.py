x = 0
total = 0
while x <= 6:
    number = input('enter a number to add to the total please: ')
    if number == 'stop':
        print ('the total is' + ' ' + str(total))
        break
    else:
        total = int(number) + total
    


