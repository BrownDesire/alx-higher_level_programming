#!/usr/bin/python3
# ANOSIKE S.C - Author
"""print the numbers from 1 to 100 separated by a space.
    For multiples of three, print frizz instead of the number
    For multiples of five, print buzz instead of the number
    Foe multiples of three and five, print FizzBuzz instead of the number
    """

def fizzbuzz():
    for number in range(1, 101):
        if number 5 % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
