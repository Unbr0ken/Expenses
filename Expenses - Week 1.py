''' Landon Weitenbeck | Assingment 1 (Expenses) | Week 10/23 - 10/29
The following program will ask for the user's input of their income and expense in order to caulctue the user's remaining blance.'''

# Varibles that save the input of the user for later use
name = input('What is your name?')
rate = float(input('What is your hourly pay rate?'))
hours1 = float(input('How many hours have you worked for week 1?'))
hours2 = float(input('How many hours have you worked for week 2?'))
hours3 = float(input('How many hours have you worked for week 3?'))
hours4 = float(input('How many hours have you worked for week 4?'))
rent = float(input('How much is rent?'))
utilities = float(input('How much do you spend on utilities?'))
transportation = float(input('How much do you spend on transportation?'))
food = float(input('How much do you spend on food?'))

#Varibles not in the user's input
CAR = 357.75        # fixed montly car payment
# Varibles that are used to calculate blances from the inputed infomation in order to get the needed infomation.
income = (hours1 + hours2 + hours3 + hours4) * rate
expense = rent + utilities + transportation + food + CAR
leftover = income - expense

# Creates Chart
# Name of Chart w/ the user's name
print()
print('Budget Report for ' + name)
print()
# Creates the list of items and their amount
print(f'{'Item':<20s}{'Amount($)':<15s}')
print(f'{'Car':<20s}{CAR:<15,.2f}')
print(f'{'Rent':<20s}{rent:<15,.2f}')
print(f'{'Utilities':<20s}{utilities:<15,.2f}')
print(f'{'Transportation':<20s}{transportation:<15,.2f}')
print(f'{'Food':<20s}{food:<15,.2f}')
print()
# Uses calculations to create a list of needed information
print(f'{'Total Income':<20s}{income:<15,.2f}')
print(f'{'Total Expense':<20s}{expense:<15,.2f}')
print(f'{'Leftover':<20s}{leftover:<15,.2f}')
