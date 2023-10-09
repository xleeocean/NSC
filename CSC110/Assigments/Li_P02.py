'''
==============================================
  Project #2 -- Bailey's Big-Batch Brownies
==============================================
Alice Li    10/04/2023
Task: Create a program to calculate the total price of ingredients Bailey will pay at the grocery store based on the number of custommers.
'''
import math

# user input
customers = int(input("How many people to be served?  "))

# Conversion rates
GRAM_TO_OZ = 1 / 28.3495231
GRAM_TO_POUND = 1 / (28.3495231 * 16)
TBSP_TO_OZ =  1 / 2

# price for ingredients per container
PRICE_COCOA_POWDER = 1.99
PRICE_SALT = 0.49
PRICE_BAKING_POWDER = 1.89
PRICE_ESPRESSO_POWDER = 5.39
PRICE_SUGAR = 1.99
PRICE_FLOUR = 1.99
PRICE_CHOCOLATE_CHIPS = 1.99
PRICE_BUTTER = 2.99
PRICE_VANILLA_EXTRACT = 10.59
PRICE_EGGS = 1.99

# calculate number of each ingredient needed
batches = math.ceil(customers / 12)

cocoa = math.ceil(batches * 106 * GRAM_TO_OZ / 8)
salt = math.ceil(batches * 6 * GRAM_TO_OZ / 26)
bakingPowder = math.ceil(batches * 5 * GRAM_TO_OZ / 8.1)
esperessoPowder = math.ceil(batches * 2 * GRAM_TO_OZ / 7.05)
sugar = math.ceil(batches * 447 * GRAM_TO_POUND / 4)
flour = math.ceil(batches * 180 * GRAM_TO_POUND / 5)
chocolateChips = math.ceil(batches * 340 * GRAM_TO_OZ / 12)
butter = math.ceil(batches * 0.5)
vanillaExtract  = math.ceil(batches * 1 * TBSP_TO_OZ / 2)
eggs = math.ceil(batches * 4 /18)

# calculate total price
totalPrice = round(PRICE_COCOA_POWDER * cocoa + PRICE_SALT * salt + PRICE_BAKING_POWDER * bakingPowder + PRICE_ESPRESSO_POWDER * esperessoPowder + PRICE_SUGAR * sugar + PRICE_FLOUR * flour + PRICE_CHOCOLATE_CHIPS * chocolateChips + PRICE_BUTTER * butter + PRICE_VANILLA_EXTRACT * vanillaExtract + PRICE_EGGS * eggs, 2)

# output grocery list
print()
print("To serve", customers, "make", batches, "batches")
print()
print("------------------------------","\n        Grocery List\n", "------------------------------", sep="")

print ("Cocoa \t\t\t", cocoa)
print("Salt \t\t\t", salt)
print("Baking Powder \t\t", bakingPowder)
print("Espresso Powder \t", esperessoPowder)
print("Sugar \t\t\t", sugar)
print("Flour \t\t\t", flour)
print("Chocolate Chips \t", chocolateChips)
print("Vanilla \t\t", vanillaExtract)
print("Eggs \t\t\t", eggs)
print("Butter \t\t\t", butter)
print()
print("Total price $ \t\t", totalPrice)


'''
----------------------------------------
                  Testing
----------------------------------------
* Test 1:
To serve 100 make 9 batches

------------------------------
        Grocery List
------------------------------
Cocoa                    5
Salt                     1
Baking Powder            1
Espresso Powder          1
Sugar                    3
Flour                    1
Chocolate Chips          9
Vanilla                  3
Eggs                     2
Butter                   5

Total price $            94.29

* Test 2
How many people to be served?  10000000

To serve 10000000 make 833334 batches


------------------------------
        Grocery List
------------------------------
Cocoa                    389484
Salt                     6784
Baking Powder            18146
Espresso Powder          8340
Sugar                    205306
Flour                    66139
Chocolate Chips          832859
Vanilla                  208334
Eggs                     185186
Butter                   416667

Total price $            6875822.35

* Test 3
How many people to be served?  one hundred
Traceback (most recent call last):
  File "/Users/oceanli/Documents/Alex/Coding Course/NSC/CSC110/Assigments/Li_P2.py", line 11, in <module>
    customers = int(input("How many people to be served?  "))
ValueError: invalid literal for int() with base 10: 'one hundred'

----------------------------------------
                Summary
----------------------------------------
Testing
- Inputs that can't be converted to int will cause error.
- There's no way to control the type of inputs for now, and there are many wanys to "break" the program.

Learning
- This program has a lot of variables. Naming is important to make sure we don't mixup the variables.
- When I was not limiting the digits of decimals, I got results with decimals like 0.000000001. I looked it up and found out it's something that related to the conversion from binary to decimals.

'''