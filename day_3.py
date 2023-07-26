# If/Else Conditionals

"""
If, Else and ElIf conditional statments used to insure that certain conditions are true in order to do a specific set of actions.

age = input("What is you age? ")

if age > 18:
In this example above we are using the if statement to determine the conditions needed to run the code indented on the next line.
  print("You can enter the store")
elif:
  print("Sorry, we didnt understand that. Try again later!)
else:
If the conditions are not true, then it will always default to the next line of code that is not in the same indented block.
  print("Sorry, come back when your older!)

  
Indetation is a big key to the structure of your code, its defines the start and end of actions set in the indented block of code from top to bottom.
"""

# Example 1 - Ticket Machine App

"""
print("Welcome to the rollercoaster!")
height = int(input("What is your heigh in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")
"""

# Comparison Operators

"""
comparison operators are used to compare data, this can be useful to determine conditional statements.

> = greater than symbol - determines if the value is greater than that of the object on the right-side of the symbol.
< = lesser than symbol - determines if the value is lesser than that of the object on the right-side of the symbol.
== = equal too - determines if both values are equal to eachother.

- adding a equal symbol alongside a comparison operator gives it two outcomes. for example:

if age >= 18:

this askes if the age is (>) greater than or (=) equal too
"""

# Nested If/Elif Statements

"""
a nested if/elif statement is a if/else statement with more than one result, it is nested inside of the same indentation block as the first if statement hence the name nested if/elif statements.

# Example - Rollercoaster Ticket App

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age in years? "))
    if age < 12:
        print("Your total fare is $5.")
    elif age >= 18:
        print("Your total fare is $12.")
    else:
        print("Your total fare is $7.")
else:
    print("Sorry, you have to grow taller before you can ride.")
"""