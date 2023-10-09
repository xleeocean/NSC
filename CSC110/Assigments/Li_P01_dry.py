'''
==============================================
          Project #1 -- CO2 Report
==============================================
Alice Li    10/02/2023
Task: Create a program to collects user information, records CO2 meter data and generates a report of results
'''

# collects user information, records CO2 meter data
def getData():

  user = {}
  user["name"] = input("Enter your name: ")
  user["date"] = input("Enter the date: ")
  print()
  homeAmCO2Reading = input("CO2 reading home (AM)? ")
  homeAmCO2Des = input("Comment for the reading: ")
  print()
  transAmCO2Reading = input("CO2 reading transportation (AM)? ")
  transAmCO2Des = input("Comment for the reading: ")
  print()
  workAmCO2Reading = input("CO2 reading work (AM)? ")
  workAmCO2Des = input("Comment for the reading: ")
  print()
  workPmCO2Reading = input("CO2 reading work (PM)? ")
  workPmCO2Des = input("Comment for the reading: ")
  print()
  transPmCO2Reading = input("CO2 reading transportation (PM)? ")
  transPmCO2Des = input("Comment for the reading: ")
  print()
  homePmCO2Reading = input("CO2 reading home (PM)? ")
  homePmCO2Des = input("Comment for the reading: ")
  print()

  co2Data = [
    ("Location", "Time", "Level", "Description"),
    ("--------", "----", "-----", "--------------------"),
    ("Home", "AM", homeAmCO2Reading, homeAmCO2Des),
    ("Transport", "AM", transAmCO2Reading, transAmCO2Des),
    ("Work", "AM", workAmCO2Reading, workAmCO2Des),
    ("", "", "", ""),
    ("Work", "PM", workPmCO2Reading, workPmCO2Des),
    ("Transport", "PM", transPmCO2Reading, transPmCO2Des),
    ("Home", "PM", homePmCO2Reading, homePmCO2Des)
  ]

  return user, co2Data

# print out the report with input data
def printResult(user, co2Data):
  print(f"{'Student name:'}\t {user['name']}")
  print(f"{'Date:'}\t\t {user['date']}")
  print("\n-->", "C a r b o n", "D i o x i d e", "R e a d i n g s",  "<--\n", sep="   ")

  for item in co2Data:
    location, time, level, description = item
    while len(location) < len("Location"):
      location += " "
    print(location, time, level, description, sep="\t")

# main function to finish the whole task
def main():
  user, co2Data = getData()
  printResult(user, co2Data)

main()


'''
---------------------------------
              Test 1
---------------------------------
Enter your name: Alice Li
Enter the date: 10/02/2023

CO2 reading home (AM)? 999
Comment for the reading: Need to open the windows

CO2 reading transportation (AM)? 600
Comment for the reading: Strong A/C is the best

CO2 reading work (AM)? 1200
Comment for the reading: I need some oxygen

CO2 reading work (PM)? 1300
Comment for the reading: I'm dying

CO2 reading transportation (PM)? 600
Comment for the reading: Yes! A/C!

CO2 reading home (PM)? 850
Comment for the reading: Fresh as it is.


------------- Output ------------

Student name:    Alice Li
Date:            10/02/2023

-->   C a r b o n   D i o x i d e   R e a d i n g s   <--

Location        Time    Level   Description
--------        ----    -----   --------------------
Home            AM      999     Need to open the windows
Transport       AM      600     Strong A/C is the best
Work            AM      1200    I need some oxygen

Work            PM      1300    I'm dying
Transport       PM      600     Yes! A/C!
Home            PM      850     Fresh as it is.

---------------------------------
              Summary
---------------------------------

• How did you approach this assignment? Where did you get stuck, and how did you get unstuck?

  For this assignment, I approached it by dividing the task into two functions: getData() and printResult(). getData() is responsible for collecting user inputs and storing them in variables, while printResult() takes these variables as parameters and formats and prints the report in the desired layout.

  I encountered three significant challenges during the assignment:

    1. Organizing CO2 Meter Data Inputs:
    To logically and clearly organize the input data, I decided to use a list of tuples. This approach made the data readable and iterable.

    2. Aligning Columns with Tabs:
    The varying lengths of location names made column alignment challenging. To address this, I implemented logic to dynamically adjust the length of the location field so that columns align correctly.

    3. Drying Out the Report Printing:
    With the reorganized CO2 data, I was able to simplify the report printing process using a loop, which made it more scalable and maintainable.


• How did you test your program? What does not work as you would like, perhaps things that you would like to fix as you learn more?

To test my program, I used two approaches. First, I quickly tested the report format by passing dummy user data to printResult(), saving me from running main() repeatedly. Second, I performed manual testing by running main() in the console. In future projects, I plan to explore writing unit tests to streamline the testing process and make it less tedious.

• What did you learn from this assignment3? What will you do differently on the next project?

From this assignment, I learned the importance of careful planning and design. Next time, I intend to allocate more time for planning and consider refactoring earlier in the process to enhance code maintainability and efficiency.
'''

