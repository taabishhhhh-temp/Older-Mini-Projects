#! /usr/bin/python3

import random

def roll():
    return random.randint(1,6)

choice = 'y'

while choice == 'y' or choice == 'Y':
    x = roll()
    if x == 1:
        print("-----------")
        print("|         |")
        print("|    1    |")
        print("|         |")
        print("-----------")
        choice = input('Enter y to roll again\nEnter any other key to finish\n\n')
        print('')

    elif x == 2:
        print("-----------")
        print("|         |")
        print("| 2     2 |")
        print("|         |")
        print("-----------")
        choice = input('Enter y to roll again\nEnter any other key to finish\n\n')
        print('')

    elif x == 3:
        print("-----------")
        print("| 3       |")
        print("|    3    |")
        print("|       3 |")
        print("-----------")
        choice = input('Enter y to roll again\nEnter any other key to finish\n\n')
        print('')

    elif x == 4:
        print("-----------")
        print("| 4     4 |")
        print("|         |")
        print("| 4     4 |")
        print("-----------")
        choice = input('Enter y to roll again\nEnter any other key to finish\n\n')
        print('')

    elif x == 5:
        print("-----------")
        print("|    5    |")
        print("| 5     5 |")
        print("| 5     5 |")
        print("-----------")
        choice = input('Enter y to roll again\nEnter any other key to finish\n\n\n')
        print('')

    elif x == 6:
        print("-----------")
        print("| 6     6 |")
        print("| 6     6 |")
        print("| 6     6 |")
        print("-----------")
        print("")
        choice = input('Enter y to roll again\nEnter any other key to finish\n\n')
        print('')

print('')
print('')
print('Thanks for Playing')
print('')
print('')