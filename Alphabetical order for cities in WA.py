#Get 2 towns from the user that are located in WA
town1 = input('Enter a town in WA: ').lstrip().capitalize()
town2 = input('Enter another town in WA: ').lstrip().capitalize()
#Compare the 2 towns (strings)
#Display the strings or towns in alphabetical order
if town1 < town2:
    print(town1)
    print(town2)
else:
    print(town2)
    print(town1)
print(input('Press Enter to Exit'))
