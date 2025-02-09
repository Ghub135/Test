import turtle


shape = input("What shape do you want? ")
length = int(input("How big should a side be? "))

if shape == 'square' or 'rectangle':
    no_of_side = 4
y = 1
while y <= no_of_side:
    turtle.forward(length)
    turtle.right(360/no_of_side)
    y=y+1
