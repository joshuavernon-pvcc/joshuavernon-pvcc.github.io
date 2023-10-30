# Name Joshua Vernon, Gabe Dyer
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees
import datetime

############ define global variables ############
# define tax rate and prices
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE= 23.5
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.9

# define global variables
inout = 1 
num_credit  = 0
scholarshipmant = 0

############ define program functions ############


def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student (Y or N)?: ")
        if yesno == "N" or yesno == "N":
            another_student = False
    
def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = int(input("Scholarship amount received:  "))

#RATE_TUITION_IN = 164.26
#RATE_TUITION_OUT = 336.21
#RATE_CAPITAL_FEE= 23.5
#RATE_INSTITUTION_FEE = 1.75
#RATE_ACTIVITY_FEE = 2.9
def perform_calculations():
    global amount,fee,total,balance, capital,institution,activity
    
    if inout == 1:
        amount  =  RATE_TUITION_IN * numcredits
        fee   = (1.75+2.9)*numcredits
        total = amount+fee
        activity  = 2.9*numcredits
        capital = 0*numcredits
        institution = 1.75*numcredits
        balance = total- scholarshipamt
    
    else:
        amount = RATE_TUITION_OUT*numcredits
        fee = (23.5+1.75+2.9)*numcredits
        total = amount + fee
        capital = 23.5* numcredits
        activity = 2.9*numcredits
        institution = 1.75*numcredits
        balance = total-scholarshipamt
    
    

def display_results():
    moneyformat = '8,.2f'
    line = '------------------------------------'
    print(line)
    print('**** PVCC ****')
    print(line)
    print('Tuition amount       $ ' + format(amount, '8,.2f'))
    print('Institutional fee    $ ' + format(institution, '8,.2f'))
    print('Capital fee          $ ' + format(capital, '8,.2f'))
    print('Student activity fee $ ' + format(activity, '8,.2f'))
    print('Total amount         $ ' + format(total, '8,.2f'))
    print('Scholarship amount   $ ' + format(scholarshipamt, '8,.2f'))
    print('Balance              $ ' + format(balance, '8,.2f'))

    print(line)
    print(str(datetime.datetime.now()))


############ call on main program to execute ############
main()
