'''
==============================================
  Project #5 -- Matchmaking
==============================================
Alice Li    11/02/2023
Task: Created a program that calculates compatibility between individuals through an algorithm that assesses users based on athleticism, eating out, entertainment out, seriousness of relationship desired, religiosity and religion, and political zeal and leaning.

'''
import math

# [0] ATHLETICISM = 0.15  [1] FOODOUT = 0.1   [2] ENTERTAINMENT = 0.15
# [3] RELATIONSHIP = 0.2  [4] RELIGION = 0.2  [5] POLITICS
WEIGHT = (0.15, 0.1, 0.15, 0.2, 0.2, 0.2)

# Create tuples for two people, call match() to determine probability, output results
def main():
  # [0]athletic, [1]foodOut, [2]entertainmentOut, [3]seriousRelationship
  # [4]religiosity, [5]religion, [6]politics zeal, [7]political leaning
  person1 = (7, 10, 8, 9, 10, "buddhism", 6, 8)
  person2 = (4, 5, 6, 10, 8, "judaism", 3, 2)

  matching = "{:.1%}".format(match(person1, person2))
  return "The probability of a compatible match is " + matching

# Matches two people to determine the probability of their compatibility
def match(p1, p2):
  match = 0
  # match for athletic, foodOut, entertainmentOut, seriousRelationship
  match += rate(p1[0], p2[0]) * WEIGHT[0]
  match += rate(p1[1], p2[1]) * WEIGHT[1]
  match += rate(p1[2], p2[2]) * WEIGHT[2]
  match += rate(p1[3], p2[3]) * WEIGHT[3]

 # match for religion
  if p1[4] >= 8 or p2[4] >= 8:
    if p1[5] == p2[5]:
      match += 1 * WEIGHT[4]
    else:
      match += 0.5 * WEIGHT[4]
  else:
    match += rate(p1[4], p2[4]) * WEIGHT[4]

  # match for polities
  if p1[6] >= 9 or p2[6] >= 9:
    match += rate(p1[7], p2[7]) * WEIGHT[5]
  else:
    match += rate(p1[6], p2[6]) * WEIGHT[5]

  return match

# rate regular categories match
def rate(rating1, rating2):
  delta = math.fabs(rating1 - rating2)

  if delta <= 1:
    rate = 1
  elif delta <= 3:
    rate = 0.7
  elif delta <= 6:
    rate = 0.4
  else:
    rate = 0

  return rate

print(main())

'''
----------------------------------------
                Summary
----------------------------------------
Planning:
- Clarity of logic is paramount in this project. To ensure comprehensive coverage of all relevant information, I used a tree map to visualize and organize the various conditions. I found that the most effective approach was to place the normal rating categories at the beginning of the index, making it straightforward to apply the appropriate conditions to the categories.

Testing:
- Testing the rate function is a straightforward process. After ensuring that the rate function works as intended, I proceed to test the match function. To do so, I systematically disable each category, assuming that the category's rating is 0. As a result, the overall match percentage is calculated as 100% minus the weight assigned to the particular category. This testing methodology was consistently applied to both religion and politics, covering all possible conditions.

Learning:
- Testing becomes increasingly challenging as the number of condition turnouts grows.
- The choice of input data structure significantly influences our approach to writing functions. A well-designed data structure greatly enhances the ease of use.

----------------------------------------
                Test Case
----------------------------------------
Please refer the test case in TestMatchmaker.py
'''