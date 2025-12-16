
number = 50

input = open("day_1_input.txt")
password = 0
for line in input: 
    direction = line[0]
    distance = int(line[1:])
    old_number = number
    if distance >= 100 :
        password += int(distance/100)
        distance = distance %100
    if direction == "R":
        number += distance

    elif direction == "L":
        number -= distance
    
    if old_number != 0 and number <= 0:
        password +=1
    elif number >=100:
        password +=1
    number = number % 100
    
    


print(password)
