cities = ["Delhi", "Karachi", "Colombo", "Dhaka", "Kabul", "Islamabad", "Dehran", "Baghdad", "Dubai"]

print(cities)

findme = input("Enter the city to be found: ")


if findme in cities:
    print(findme + " " + "is present")

else:
    print(findme + " " + "is not present")


i = len(cities)
i = i - 1
print(i)
found = False

while i >= 0:
    if cities[i] == findme:
        print(findme + " " + "is present in while loop")
        found = True
        break
    i = i - 1

 


    
