'''
==============================================
        Project #6 -- CO2 Data Entry & Stats
==============================================
Alice Li    11/13/2023
Task: Prompt users with questions to gather input data related to CO2. Validate the provided inputs to ensure accuracy. Perform calculations based on the collected data and display the results.
'''

# Calls enterCo2ReadingBatch, receives its returned data, and prints the report
def main():
  name, location, minLevel, maxLevel, readingCount, avgLevel = enterCo2ReadingBatch()

  # Take care readingCount's initial value when readingCount == 0
  if readingCount == 0:
    minLevel = 0

  print("\n--------------------------------------------------")
  print("Recorder name: \t \t", name)
  print("Reading location:\t", location, "\n")
  print("Number of readings:\t", readingCount)
  print("Minimum CO2 Level:\t", minLevel)
  print("Maximum CO2 Level:\t", maxLevel)
  print("Average CO2 level:\t", round(avgLevel))
  print("--------------------------------------------------\n")

# Performs data entry, returns statistics
def enterCo2ReadingBatch():
  name = getNonEmptyString("Enter name: ")
  location = getNonEmptyString("Enter location: ")

  # Declare variables with initial value
  readingCount = 0
  minLevel = 10000
  maxLevel = 0
  sumOfLevel = 0
  avgLevel = 0

  month = getInRangeInteger(0, 12, "\nEnter month (or 0 to exit): ")
  while (month != 0):
    day = getInRangeInteger(1, 31, "Enter day: ")
    year = getInRangeInteger(2022, 2099, "Enter year: ")
    co2Reading = getInRangeInteger(1, 10000, "Enter CO2 reading: ")

    readingCount += 1
    sumOfLevel += co2Reading
    avgLevel = sumOfLevel / readingCount

    if minLevel > co2Reading:
      minLevel = co2Reading

    if maxLevel < co2Reading:
      maxLevel = co2Reading

    month = getInRangeInteger(0, 12, "\nEnter month (or 0 to exit): ")

  return name, location, minLevel, maxLevel, readingCount, avgLevel


# Asks the user for data, validates it (keeps pestering the user until they comply), and returns an integer guaranteed to be in the specified range
def getInRangeInteger(minValueAllowed, maxValueAllowed, prompt):
  validInt = input(prompt)

  while (validInt.isdigit() == False or int(validInt) < minValueAllowed or int(validInt) > maxValueAllowed):
    print("Please enter a valid integer.")
    validInt = input(prompt)

  return int(validInt)

# Asks the user for data, validates it (keeps pestering the user until they comply), and returns a non-empty string
def getNonEmptyString(prompt):
  validString = input(prompt)

  while validString == "":
    print("Enter can not be empty.")
    validString = input(prompt)

  return validString

main()

'''
======================================
              Summary
======================================
Planning:
- Nothing special on planning
- What got me stucked was validating user input to ensure it could be successfully converted into an integer. Since the `try` mechanism had not been covered, I opted for using the `string.isdigit()` method for validation.

Testing:
- Four key considerations guided my testing process:
  1. getNonEmptyString: Ensured that the prompt persisted for inputs when the user provided an empty string.
  2. getInRangeInteger: Ensured that the prompt persisted for inputs that could not be converted into an integer.
  3. getInRangeInteger: Ensured that the prompt persisted for inputs outside the specified range.
  Since I test 2, 3 at the same time, .isdigit() before range check is essential
  4. enterCo2ReadingBatch: Implemented a condition for the function to exit only when the input for the month equals 0.

Learning:
- It can be a bit challenging to transition between various types of loops. Initially, I contemplated using a do-while loop, only to discover that Python does not support this construct. Consequently, I experimented with a while True loop combined with an if statement with break keyword, which proved effective. Subsequently, I refactored the code to employ a while not condition loop. It's intriguing to observe that despite their structural differences, loops can encapsulate the same logic. The declaration scope of variables and determining the exit point are often the aspects prone to causing issues.
- day and year data was collected bt never used

======================================
          Test case 1
======================================
Enter name: gsfdg
Enter location: fgaserg

Enter month (or 0 to exit): 12
Enter day: 12
Enter year: 2045
Enter CO2 reading: 3423

Enter month (or 0 to exit): 9
Enter day: 24
Enter year: 2032
Enter CO2 reading: 4365

Enter month (or 0 to exit): 0

--------------------------------------------------
Recorder name:           gsfdg
Reading location:        fgaserg

Number of readings:      2
Minimum CO2 Level:       3423
Maximum CO2 Level:       4365
Average CO2 level:       3894
--------------------------------------------------

======================================
          Test case 2
======================================
Enter name:
Enter can not be empty.
Enter name: fasd
Enter location:
Enter can not be empty.
Enter location: gregog ggdf

Enter month (or 0 to exit): not int
Please enter a valid integer.

Enter month (or 0 to exit): 15
Please enter a valid integer.

Enter month (or 0 to exit): 3
Enter day: not int
Please enter a valid integer.
Enter day: 351
Please enter a valid integer.
Enter day: 0
Please enter a valid integer.
Enter day: 23
Enter year: not int
Please enter a valid integer.
Enter year: 1000
Please enter a valid integer.
Enter year: 2035
Enter CO2 reading: not int
Please enter a valid integer.
Enter CO2 reading: 3451

Enter month (or 0 to exit): 0

--------------------------------------------------
Recorder name:           fasd
Reading location:        gregog ggdf

Number of readings:      1
Minimum CO2 Level:       3451
Maximum CO2 Level:       3451
Average CO2 level:       3451
--------------------------------------------------

======================================
          Test case 3
======================================
Enter name: my name
Enter location: my location

Enter month (or 0 to exit): 0

--------------------------------------------------
Recorder name:           my name
Reading location:        my location

Number of readings:      0
Minimum CO2 Level:       0
Maximum CO2 Level:       0
Average CO2 level:       0
--------------------------------------------------

'''
