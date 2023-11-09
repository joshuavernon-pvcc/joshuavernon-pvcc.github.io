# Name: Joshua Vernon
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
#-----------------------------
# Canine Vaccines:
#   1. Bordatella       $30.00
#   2. DAPP             $35.00
#   3. Influenza        $48.00
#   4. Leptospirosis    $21.00
#   5. Lyme Disease     $41.00
#   6. Rabies           $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew; one chew per month)
#   Small dogs, Up to 25 lbs:         $9.99
#   Medium-sized dogs, 26 t0 50 lbs:  $11.99
#   Large dogs: 51 to 100 lbs:        $13.99
#-----------------------------------------------------------
# Cat Vaccines:
#   1.  Feline Leukemia                 $35.00
#   2.  Feline Viral Rhinotracheitis    $30.00
#   3.  Rabies                          $25.00
#   4.  Feline Vaccine Package (includes all vaccines): 10% discount
#   
# Feline Heartworm Preventative Chews (one size): $8.00

import datetime
from functools import total_ordering

######### define global variables #########
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEPTO = 21
PR_LYME = 41
PR_RABIES = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

#define cat prices
PR_FEL_LEUK = 35
PR_FEL_RHINO = 30
PR_RABIES = 25

PR_CAT_ALL = 0

PR_CAT_CHEWS = 8.00

########### define program functions ############
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper90 == "N" :
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog (D) or cat (C)? ")
    pet_weight = int(input("Weight of your pet (in pounds): "))

########### DOG Functions ###################

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.NONE"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is reccommended for all dogs.")
    heart_yesno = input("\tWould you like to order monthly heartworm medication for " + pet_name + " (Y/N) ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("\tHow many heart worm chews would you like to order? "))

def perform_dog_calculations():
    global vax_cost, vax_name, chews_cost, total, PR_ALL

    #### vaccines

    if pet_vax_type == 1 :
        vax_cost = PR_BORD
        vax_name = "Bordatella"

    elif pet_vax_type == 2 :
        vax_cost = PR_DAPP
        vax_name = "DAPP"

    elif pet_vax_type == 3 :
        vax_cost = PR_FLU
        vax_name = "Influenza"

    elif pet_vax_type == 4:
        vax_cost = PR_LEPTO
        vax_name = "Leptospirosis"

    elif pet_vax_type == 5:
        vax_cost = PR_LYME
        vax_name = "Lyme Disease"

    elif pet_vax_type == 6:
        vax_cost = PR_RABIES
        vax_name = "Rabies"

    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEPTO + PR_LYME + PR_RABIES
        vax_cost = 0.85 * PR_ALL
        vax_name = "Full Vax Package"

    ####### heart worm chews
    if num_chews != 0 :
        if pet_weight < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL

        elif pet_weight >= 26 and pet_weight < 50 :
            chews_cost = num_chews * PR_CHEWS_MED

        else:
            chews_cost = num_chews * PR_CHEWS_LARGE

    ######### find total
    total = vax_cost + chews_cost

def display_dog_results():
    line = '--------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** Dog & Cat Clinic ****')
    print('Your local veterinarian')
    print(line)
    print('Vaccine            $ ' + format(vax_name,moneyf))
    print('Vaccine Cost       $ ' + format(vax_cost,moneyf))
    print('Chews Cost         $ ' + format(chews_cost,moneyf))
    print('Total              $ ' + format(total,moneyf))
    print(str(datetime.datetime.now()))

############ CAT functions ################
def get_cat_data():
   global cat_vax_type, cat_num_chews
   cat1 = "\n** Cat Vaccines:\n\t1. Feline Leukemia\n\t2. Feline Viral Rhinotracheitis\n\t3. Rabies\n\t4. Feline Vaccine Package\n\t5. NONE"
   catmenu = cat1
   cat_vax_type = int(input(catmenu + "\n** Enter the vaccine number: ")) 

def perform_cat_calculations():
    global cat_vax_cost, cat_vax_name, cat_chews_cost, cat_total, PR_CAT_ALL

    if cat_vax_type == 1:
        cat_vax_cost = PR_FEL_LEUK
        cat_vax_name = "Feline Leukemia"

    elif cat_vax_type == 2:
        cat_vax_cost = PR_FEL_RHINO
        cat_vax_name = "Feline Viral Rhinotracheitis"

    elif cat_vax_type == 3:
        cat_vax_cost = PR_RABIES
        cat_vax_name = "Rabies"

    else:
        cat_vax_type == 4:
        PR_CAT_ALL = PR_FEL_LEUK + PR_FEL_RHINO + PR_RABIES
        cat_vax_cost = 0.90 * PR_CAT_ALL
        cat_vax_name = "Feline Vaccine Package"

    cat_total = cat_vax_cost + cat_chews_cost
        
def display_cat_results():
    line = '--------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** Dog & Cat Clinic ****')
    print('Your local veterinarian')
    print(line)
    print('Vaccine            ' + cat_vax_name)
    print('Vaccine Cost       $ ' + format(cat_vax_cost,moneyf))
    print('Chews Cost         $ ' + format(cat_chews_cost,moneyf))
    print('Total              $ ' + format(cat_total,moneyf))
    print(str(datetime.datetime.now()))



############# call on main program to execute ###############
main()

