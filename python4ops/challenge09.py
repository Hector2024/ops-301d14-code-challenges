'''
OBJECTIVE:
Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b

Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

Create an if statement that includes both elif and else to execute when both if and elif are not met.

'''
# This takes user input for a & b and checks if they are integers
while True:
    try:
        a = int(input("Please enter a number: "))
        b = int(input("Please enter a second number: "))
        c = int(input("Please enter the last number: "))
        print("You entered: {}, {}, and {}".format(a, b, c))
        break
    except ValueError:
        print("That was not a number, please try again.")
    except EOFError:
        print("You did not enter anything, please try again.")
        break

# This checks a against be and prints out the result

if a < b:
    print("a is less than b.")
elif a > b:
    print("a is greater than b.")
elif a == b:
    print("a is equal to b.")
else:
    print("a is not equal to b.")
if b <= c:
        print("b is less than or equal to c")
elif b >= c:
        print("b is greater than or equal to c")
else:
     print("b is equal to c") 


'''
Pursue stretch goals if you are a more advanced user or have remaining lab time.

Create an if statement with two conditions by using and between conditions.

Create an if statement with two conditions by using or between conditions.

Create a nested if statement.

Create an if statement that includes pass to avoid errors.
'''


if a == b and c < b:
     print("c is less than both a and b")
elif a > b or b < c:
     print("b is less than either a and c")
     if a == b and b == c:
          print("all numbers are equal")
          if a < b and b > c:
               pass
else:
    print("Im not doing more math, bye! ")