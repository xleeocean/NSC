'''
==============================================
  Project #3 -- Program Template Generator
==============================================
Alice Li    10/10/2023
Task: Implement call hierarchy program to make headers and section headers for your programs according to the user inputs
'''

# global variables
BANNER_WIDTH = 45
userName = ""
date = ""
programName = ""
description = ""

# define functions
def main():
  collectInputs()
  displayBanner()
  displaySectHeaders()

def collectInputs():
  global userName
  global date
  global programName
  global description
  userName = input("Enter your name: ")
  date = input("Enter the date: ")
  programName = input("Enter the program name: ")
  description = input("Enter short description: ")

def displayBanner():
  displayStarLine()
  print("#\t", "Coder\t:", userName)
  print("#\t", "Date\t:", date)
  print("#\t", "Program:", programName)
  print("#\t", "Descrip:", description)
  displayStarLine()
  print("\t")

def displaySectHeaders():
  displaySectHeader("Constants")
  displaySectHeader("Variables")
  displaySectHeader("Input")
  displaySectHeader("Processing")
  displaySectHeader("Output")

def displaySectHeader(SectionName):
  displayStarLine()
  print("#\t", SectionName)
  displayStarLine()
  print("\n")

def displayStarLine():
  print("#" + "*" * (BANNER_WIDTH - 1))

# call function
main()

'''
----------------------------------------
                  Testing
----------------------------------------
* Test 1
  input:
  Enter your name: Bill Barry
  Enter the date: 10/02/19
  Enter the program name: Circle Geometry
  Enter short description: Given circle radius, calculate area & volume

  output:
  #********************************************
  #        Coder  : Bill Barry
  #        Date   : 10/02/19
  #        Program: Circle Geometry
  #        Descrip: Given circle radius, calculate area & volume
  #********************************************

  #********************************************
  #        Constants
  #********************************************


  #********************************************
  #        Variables
  #********************************************


  #********************************************
  #        Input
  #********************************************


  #********************************************
  #        Processing
  #********************************************


  #********************************************
  #        Output
  #********************************************

* Test 2
  input:
  Enter your name: long long long long long long long long long long longlong long long long long long long long long long longlong long long long long long long long long long long
  Enter the date: long long long long long long long long long long longlong long long long long long long long long long longlong long long long long long long long long long long
  Enter the program name: long long long long long long long long long long longlong long long long long long long long long long long
  Enter short description: long long long long long long long long long long longlong long long long long long long long long long longlong long long long long long long long long long long

  output:
  #********************************************
  #        Coder  : long long long long long long long long long long longlong long long long long long long long long long longlong long long long long long long long long long long
  #        Date   : long long long long long long long long long long longlong long long long long long long long long long longlong long long long long long long long long long long
  #        Program: long long long long long long long long long long longlong long long long long long long long long long long
  #        Descrip: long long long long long long long long long long longlong long long long long long long long long long longlong long long long long long long long long long long
  #********************************************

  #********************************************
  #        Constants
  #********************************************


  #********************************************
  #        Variables
  #********************************************


  #********************************************
  #        Input
  #********************************************


  #********************************************
  #        Processing
  #********************************************


  #********************************************
  #        Output
  #********************************************

----------------------------------------
                Summary
----------------------------------------
Planning:
- I outlined the project's structure using comments and then created functions accordingly. Something got me stucked.

Testing:
- I individually tested each function by calling them separately before testing the main function.
- Maintaining the perfect format can be challenging when the input is too long. I can format it to a specific length, but this might result in truncated display. For perfect formatting, the program can become more complex. It may require adding conditional logic to detect long strings, breaking them into smaller pieces, and inserting '#' and space before each piece.

Learning:
- Breaking a large project into functions improves organization and enables code reuse.
- In this project, we relied on global variables, eliminating the need to pass variables through function parameters. However, in more complex projects, it becomes challenging to track which functions alter global variables and maintain data integrity.

'''