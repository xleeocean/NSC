'''
==============================================
  Project #4 -- Common Math Formulas
==============================================
Alice Li    10/23/2023
This project takes user inputs, utilizes a supplier program to perform the following calculations, \
and prints the results:
- Calculate the distance between two points.
- Determine the midpoint of two points.
- Compute the radius between a center point and another point.
'''

from formulas import calcDistance
from formulas import calcMidpoint
from formulas import calcRadius

BANNER_WIDTH = 50

def main():
  doDistancePractice()
  print()
  doMidpointPractice()
  print()
  doRadiusPractice()
  print()
  print("That wraps up practice time. See you next time!\n")

def doDistancePractice():
  printBanner("DISTANCE PRACTICE")
  x1 = float(input("Enter x1: "))
  y1 = float(input("Enter y1: "))
  x2 = float(input("Enter x2: "))
  y2 = float(input("Enter y2: "))
  distance = calcDistance(x1, y1, x2, y2)
  print("Distance =", distance)

def doMidpointPractice():
  printBanner("MIDPOINT PRACTICE")
  x1 = float(input("Enter x1: "))
  y1 = float(input("Enter y1: "))
  x2 = float(input("Enter x2: "))
  y2 = float(input("Enter y2: "))
  midX, midY = calcMidpoint(x1, y1, x2, y2)
  print("Midpoint x =", midX)
  print("Midpoint y =", midY)

def doRadiusPractice():
  printBanner("RADIUS PRACTICE")
  x1 = float(input("Enter center x: "))
  y1 = float(input("Enter center y: "))
  x2 = float(input("Enter point x: "))
  y2 = float(input("Enter point y: "))
  r = calcRadius(x1, y1, x2, y2)
  print("Radius = ", r)

def printBanner(bannerName):
  print("-" * BANNER_WIDTH)
  print(bannerName.center(BANNER_WIDTH) )
  print("-" * BANNER_WIDTH)

main()


'''
----------------------------------------
                Summary
----------------------------------------
Planning:
- There's nothing particularly unique about the planning phase of this project. \
  I outlined the project's structure using comments and started working as usual.

Testing:
- During testing, I called each function individually after completing it to ensure \
  that they worked correctly on their own.
- When creating unit tests, I found that specifying the type and format of the expected output was crucial. \
  I used the format() function, which converts a float into a string. This initially caused test failures\
  until I adjusted the expected output to match the exact format.

Learning:
- I realized that calcDistance and calcRadius are essentially the same thing.
- The user experience of this program is less than optimal. Whenever the user makes a typographical error\
  in the input, the program crashes, forcing the user to start over.

'''