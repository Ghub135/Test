import turtle

draw_shape = 'yes'
while draw_shape == 'yes': 
    shape = input("What shape do you want? ")
    length = int(input("How big should a side be? "))
    
    if shape == 'square' or 'rectangle':
        no_of_side = 4
    if shape == 'triangle':
        no_of_side = 3
    if shape == 'pentagon':
        no_of_side = 5
    if shape == 'hexagon':
        no_of_side = 6
    if shape == 'octagon':
        no_of_side = 8

    y = 1
    while y <= no_of_side:
        turtle.forward(length)
        turtle.right(360/no_of_side)
        y=y+1

    
    draw_shape = input("Draw another shape? ")
    turtle.clear()

    
        
        
    
    
    
