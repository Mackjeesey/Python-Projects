#Get the tax rate from the user
tax = float(input("Please enter the tax rate: "))
#Convert tax rate to a percentage and add 1
tax = tax/100+1
#Get the item's price
price = float(input("Please enter the items price: "))
#Apply the tax to the price
price = price*tax
#Display the total price
print('The total price is $',format(price, '.2f'),sep='')
print(input('Press enter to exit.'))
