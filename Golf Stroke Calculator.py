# Loops entire program in the event user wanted to check multiple holes
while True:
    # Get hole number from the user while rejecting anything other than whole numbers
    try:
        holenum = int(input('Please enter the hole number: '))
    except ValueError:
        print('Oops! Whole numbers only please. Restarting program.')
        continue
    # Get par value for the hole while rejecting anything other than whole numbers
    try:
        par = int(input('Please enter the par value for the hole: '))
    except ValueError:
        print('Oops! Whole numbers only please. Restarting program.')
        continue
    # Get number of strokes user took for hole while rejecting anything other than whole numbers
    try:
        strokes = int(input('Please enter the number of strokes it took to complete the hole: '))
    except ValueError:
        print('Oops! Whole numbers only please. Restarting program.')
        continue
    # Subtract number of strokes user took from par value and display appropriate term
    final = strokes - par
    if final < -5:
        print('Wow, there is not a golf term for that one. Impressive.')
    elif final == -5:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Ostrich.')
    elif final == -4:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Condor.')
    elif final == -3:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Albatross.')
    elif final == -2:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Eagle.')
    elif final == -1:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Birdie.')
    elif final == 0:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Par.')
    elif final == 1:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Bogey.')
    elif final == 2:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Double Bogey.')
    elif final == 3:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a Triple Bogey.')
    elif final == 4:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a 4 over Par.')
    elif final == 5:
        print('On hole number', holenum, 'which is a par', par, 'you recorded', strokes, 'strokes. You got a 5 over Par.')
    else:
        print('Bad Score.')
# Adds in option to restart the program while rejecting everything except a 1 or 2
    while True:
        try:
            redo = int(input('Press 1 to enter a new hole or 2 to exit: '))
        except ValueError:
            print('Enter 1 or 2 only please.')
            continue
        if redo == 1:
            print('Restarting program as directed.')
            break
        elif redo == 2:
            break
        else:
            print('Enter 1 or 2 only please.')
            continue
    # This additional if closes the program
    if redo == 2:
        break
