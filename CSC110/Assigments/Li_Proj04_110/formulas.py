'''
==============================================
  Project #4 -- Common Math Formulas
==============================================
Alice Li    10/23/2023
formulas.py is a code module that acts as a supplier of functions. It takes parameters and performs\
calculations when the functions are called
'''

# calcDistance takes the coordinates of point1 and point2,
# and returns the distance between the two points.
def calcDistance(x1, y1, x2, y2):
  distance = format((((x2 - x1)**2 + (y2 - y1)**2)**0.5), ".4f")
  return distance

# calcMidpoint takes coordinates of point1 and point2,
# and returns the coordinates of the midpoint between the two points.
def calcMidpoint(x1, y1, x2, y2):
  midpointX =  format(((x1 + x2) / 2), ".4f")
  midpointY =  format(((y1 + y2) / 2), ".4f")
  return midpointX, midpointY

# calcRadius takes the coordinates of the center and a point,
# and returns the radius of the circle
def calcRadius(centerX, centerY, pointX, pointY):
  radius =  format(((pointX - centerX)**2 + (pointY - centerY)**2)**0.5, ".4f")
  return radius





