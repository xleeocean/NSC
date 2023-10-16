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
  global userName, date, programName, description
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
                Summary
----------------------------------------
Planning:
- I outlined the project's structure using comments and then created functions accordingly. Nothing got me stucked.

Testing:
- I individually tested each function by calling them separately before testing the main function.
- Maintaining the perfect format can be challenging when the input is too long. I can format it to a specific length, but this might result in truncated display. So , use format funciton doesn't seems nessecery here. For perfect formatting, the program can become more complex. It may require adding conditional logic to detect long strings, breaking them into smaller pieces, and inserting '#' and space before each piece.

Learning:
- Breaking a large project into functions improves organization and enables code reuse.
- In this project, we relied on global variables, eliminating the need to pass variables through function parameters. However, in more complex projects, it becomes challenging to track which functions alter global variables and maintain data integrity.

'''