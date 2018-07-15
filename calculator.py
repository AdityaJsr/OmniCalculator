# my first attempt to create a calculator.
# A simple calculator using Python.

import re

print("The OmniCalC")
print("Enter 'quit' to exit \n")

previous = 0
run = True


def do_math():
    global run
    global previous

    equation=""
    exit = ['Quit', 'quit', 'QUIT']
    if previous==0:
        equation = input("Enter the equation:")
    else:
        equation = input(str(previous))
    if equation in exit:
        run = False
    else:
        equation = re.sub('[A-Z a-z:/?<>!@#%&*" "]','', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = input(str(previous))

        print("You Entered", previous)


while run:
    do_math()
