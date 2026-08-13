# a program that estimates the horsepower needed to cool a room with an air conditioner. 
area = float(input("Enter the room area in square feet:"))
horsepower = (area * 20) / 9000 #the 20 is BTU = british terminal units, and 9000 is the BTU per horsepower for smaller room

print(f"the estimated horsepower needed to cool the room is {horsepower:.2f} HP")
