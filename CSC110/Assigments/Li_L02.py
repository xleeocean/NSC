# CSC 110 Lab2
# Program to gets a measurement from the user in feet and displays that value in feet and inches as separate numbers
# Alice Li

# input
userInput = float(input("Enter the number in feet you want to convert: "))

# convert
feet = int(userInput)
inches = (userInput - feet) * 12

# output
print(userInput, "feet is equivalent to", feet, "feet", format(inches,".1f"), "inches")