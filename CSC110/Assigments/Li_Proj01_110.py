'''
==============================================
          Project #1 -- CO2 Report
==============================================
Alice Li    10/02/2023
Task: Create a program to collects user information, records CO2 meter data and generates a report of results
'''

# collects user information, records CO2 meter data
name = input("Enter your name: ")
date = input("Enter the date: ")
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
print()

# print out the report with input data
print("Student name:\t", name)
print("Date:\t\t", date)
print("\n-->", "C a r b o n", "D i o x i d e", "R e a d i n g s",  "<--\n", sep="   ")
print("Location", "Time", "Level", "Description", sep="\t")
print("--------", "----", "-----", "--------------------", sep="\t")
print("Home\t", "AM", homeAmCO2Reading, homeAmCO2Des, sep="\t")
print("Transport", "AM", transAmCO2Reading, transAmCO2Des, sep="\t")
print("Work\t", "AM", workAmCO2Reading, workAmCO2Des, sep="\t")
print()
print("Work\t", "PM", workPmCO2Reading, workPmCO2Des, sep="\t")
print("Transport", "PM", transPmCO2Reading, transPmCO2Des, sep="\t")
print("Home\t", "PM", homePmCO2Reading, homePmCO2Des, sep="\t")


'''
---------------------------------
              Test 1
---------------------------------
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

  For this assignment, I approached it by dividing the task into two parts: pert1 is responsible for collecting user inputs and storing them in variables, while part2 prints the report in the desired layout.

  I encountered one challenges when aligning Columns with Tabs. The varying lengths of location names made column alignment challenging. To address this, I had to add space to shorter names of the location so that columns align correctly.


• How did you test your program? What does not work as you would like, perhaps things that you would like to fix as you learn more?

To test my program, I used two approaches. I tested the part2 of code by assigning dummy values to the variables, saving me from inputing in the console repeatedly. Second, I performed manual testing by running the programe in the console. In future projects, I plan to explore writing unit tests to streamline the testing process and make it less tedious.

• What did you learn from this assignment? What will you do differently on the next project?

From this assignment, I used to use some knowledge that's not covered in week1, so I did it again. Next time, I'll try to use only the material that has been covered in class.
'''

