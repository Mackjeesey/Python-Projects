import time     # To use time delay to display results
fact = 1        # For factorial calculation
sum = 0         # For sum function
# Something to spice up the beginning of the program
print('Welcome to Integer Fun! The following program might be helpful if you have very specific desires regarding manipulations of non-negative integers.')
time.sleep(3)
print('Right tool for the right job kind of thing I suppose.')
time.sleep(3)
print('Well anyways without further ado lets get into it in...')
time.sleep(3)
count = 3
while count > 0:
    print(count)
    count -= 1
    time.sleep(1)
    if count == 0:
        continue
# The purpose of this loop allows the user to select another number without having to re-open the program
while True:
    # Loops non-negative entry block
    while True:
        try:
            num = int(input('Please enter a non-negative integer: \n'))
            # Rejects negative numbers
            if num < 0:
                print('Non-negative integers only please. Restarting program')
                continue
            # Continues on if a non-negative number entered
            else:
                break
        # Rejects everything else besides an integer
        except ValueError:
            print('Non-negative integers only please. Restarting program')
            continue
# Loops menu allowing to re-use the same number
    while True:
        print('Please select an option from the list provided using the numbers 1, 2, 3, 4, or 0.\n1. Display the integers from 0 to your entered integer, counting by 5\n2. Display the sum of the integers starting from 1 to the integer entered\n''3. Display the factorial of the integer\n4. Enter a new non-negative integer\n0. Quit Program')
        try:
            choice = int(input("Enter your menu choice: "))
            # Rejects negative numbers
            if choice < 0:
                print('You have selected an option outside the list. Please try again.')
                time.sleep(3)
                continue
            # rejects numbers greater than 3
            elif choice >= 5:
                print('You have selected an option outside the list. Please try again.')
                time.sleep(3)
                continue
            # Option to quit program
            elif choice == 0:
                print('Until next time.')
                time.sleep(3)
                exit()
            # Displays 1 to number entered counting by 5
            elif choice == 1:
                for i in range(0, num + 1, 5):
                    print(i)
                # if the number is less than 5 and therefore would only display one number a comment is made
                if num < 5:
                    print('Hmm, could have guessed this would be the outcome, eh?')
                time.sleep(3)
                continue
            # Sum of integers from 1 to the number entered
            elif choice == 2:
                for i in range(1, num + 1):
                    sum = sum + i
                print('The sum of the numbers between 1 and', num, 'is: ', end='')
                print(sum)
                time.sleep(3)
                continue
            # Factorial calculation
            elif choice == 3:
                for i in range(1, num + 1):
                    fact = fact * i
                print('The factorial of', num, 'is: ', end='')
                print(fact)
                time.sleep(3)
                continue
            elif choice == 4:
                print('Returning to selection section')
                time.sleep(3)
                break
        # Rejects anything other than an integer entry
        except ValueError:
            print('You have selected an option outside the list. Please try again.')
            time.sleep(3)
            continue
