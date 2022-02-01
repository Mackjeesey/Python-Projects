# Fun intro for user asking them a question, if answer yes continue if anything else loop back
while True:
    answer = input('Tired of Basic Math? Enter Yes or No: ').lstrip().lower()
    if answer == 'yes':
        print('Everyone is! Please continue for the solution to your problem.')
        break
# add in catch for if the user enters anything else
    else:
        print('Error: Impossible Answer. Please try again.')
# User provides number. in the case of an undesired answer a loop occurs
while True:
    try:
        numone = int(input('Pick a Whole Number: '))
        break
    except ValueError:
        print('Oops! Whole Numbers Only, Please Try Again.')
        continue
# User provides another number with loop in the case of an undesired answer
while True:
    try:
        numtwo = int(input('Pick a Second Whole Number (Repeats Allowed): '))
        break
    except ValueError:
        print('Oops! Whole Numbers Only, Please Try Again.')
# Sum of numbers 1 and 2
sum = numone+numtwo
print(numone, '+', numtwo, '=', sum, '.', sep='')
# Difference between numbers 1 and 2
diff = numone-numtwo
print(numone, '-', numtwo, '=', diff, '.', sep='')
# Product of numbers 1 and 2
prod = numone*numtwo
print(numone, '*', numtwo, '=', prod, '.', sep='')
# First number raised to the second number
exp = numone**numtwo
print(numone, '^', numtwo, '=', exp, '.', sep='')
# Integer division of the first number by the second with catch to prevent division by 0
if numtwo != 0:
    quo = numone // numtwo
    rem = numone % numtwo
    print(numone, '/', numtwo, '=', quo, ' with a remainder of ', rem, '.', sep='')
else:
    print('Cannot divide by zero')
print('Thank you for playing!')
input('Press Enter to Exit. ')
