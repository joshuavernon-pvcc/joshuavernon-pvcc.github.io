# NAME: Joshua Vernon 
# Prog purpose: This program finds the tax of a car 
#   Personal property rate: $4.20 per $100 of vehicle value (4.20% per year)
#   Tax relief: 33%

import datetime

########## define global variables ##########
# define tax rate and prices
PERSONAL_PROPERTY_RATE = 0.042
TAX_RELIEF = 0.33

# define global variables
car_value = 0
annual_tax_amount = 0
relief_amount = 0

##### define program functions #####
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to calculate the tax again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False
            print("Thank you for using this program!")

def get_user_data():
    global car_value, eligible_tax_relief
    car_value = int(input("What is the cars value?: "))
    eligible_tax_relief = str(input("Is the car eligible for tax relief?(Y/N): "))

def perform_calculations():
    global car_value, annual_tax_amount, relief_amount

    if eligible_tax_relief.upper() == "N" :
        annual_tax_amount = ((car_value * PERSONAL_PROPERTY_RATE)/2)
        relief_amount = 0

    elif eligible_tax_relief.upper() == "Y" :
        annual_tax_amount = ((car_value * PERSONAL_PROPERTY_RATE)/2)
        relief_amount = (car_value * PERSONAL_PROPERTY_RATE * TAX_RELIEF)
        annual_tax_amount = (annual_tax_amount - relief_amount)


def display_results():
    line = '--------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** Personal Property Tax ****')
    print(line)
    print('Car Value                $ ' + format(car_value,moneyf))
    print('Annual Amount Owed       $ ' + format((annual_tax_amount*2),moneyf))
    print('Relief Amount            $ ' + format(relief_amount,moneyf))
    print('Amount Due               $ ' + format((annual_tax_amount),moneyf))
    print(str(datetime.datetime.now()))

###### call on main program to execute ########
main()



