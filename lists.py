fruit = ['apple', 'banana', 'cherry', 'damson', 'grape', 'kiwi', 'melon']

print (fruit)

fruit_choice = input('what fruit are you looking for: ')

if fruit_choice in fruit:
    print ('the fruit ' + fruit_choice + ' is already there')
else:
    print (fruit)
    fruit.append(fruit_choice)
    print ('the fruit ' + fruit_choice + ' is appended')
    print (fruit)
    fruit.insert(0,'inserted_fruit')
    print (fruit)
    fruit.remove('inserted_fruit')
    print (fruit)

    i = 0
    while i < len(fruit):
        print (fruit[i])
        i = i+1

    for x in fruit:
        print(x)

    print ("all done")
