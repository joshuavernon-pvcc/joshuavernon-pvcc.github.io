# Name Joshua Vernon
# Prog Purpose: This program computes hotel guest costs based on
#   room type, number of nights, and sales/occupancy tax rates

import datetime

############ define global variables ############
# define tax rate and prices
SR = 195.00
DR = 250.00
SU = 350.00
SALES_TAX = 0.065
OCC_TAX = 0.1125


subtotal = 0
room_type = 0
num_night = 0
sales_tax = 0
occ_tax = 0
total = 0
cust = []
outfile = 'hotelsalesrep.html'

############ define program functions ############
def main():
    open_outfile()
    read_in_cust_file()
    grand_total = perform_calculations()  
    display_cust_list()

    print('\n** Open this file in a browser window to see your results: ' + outfile)


def read_in_cust_file(filename="emerald.csv"):
        with open(filename, "r", newline="") as file:
            for line in file:
                cust.append(line.strip().split(','))



def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style>\n')
    f.write('<style> body{background-color: #87CEEB; background-image: url("beach_wallpaper.jpg"); background-repeat: no-repeat; background-size: 100% 100%; color: #333;}\n')
    f.write('</style></head>\n')
    f.write('<body>\n')
    f.write('<center>\n')  



def perform_calculations():
    global subtotal, occ_tax, sales_tax, total

    grand_total = 0  

    for guest in cust:
        room_type_code = guest[2]
        num_night = int(guest[3])

        if room_type_code == "SR":
            subtotal = SR * num_night
        elif room_type_code == "DR":
            subtotal = DR * num_night
        else:
            room_type_code == "SU"
            subtotal = SU * num_night

        
        sales_tax = subtotal * SALES_TAX
        occ_tax = subtotal * OCC_TAX
        total = subtotal + sales_tax + occ_tax

        
        guest.extend([subtotal, sales_tax, occ_tax, total])

        grand_total += total  

    return grand_total  


def display_cust_list():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    f.write('\n<table border="3" style="background-color: #D2B48C; font-family: arial; margin: auto;">\n')
    
    
    f.write('<tr><th colspan="7" style="background-color: #87CEEB; color: #006400;">')
    f.write('<h2>Emerald Beach & Hotel Resort</h2></th></tr>')
    
    
    f.write('<tr><th colspan="7" style="background-color: #87CEEB; color: #006400;">')
    f.write('Sales Report Date/Time: ' + day_time + '</th></tr>')


    f.write('<tr style="background-color: #87CEEB; color: #006400;">')
    f.write('<th>Last Name</th><th>First Name</th><th>Num Nights</th>' +
            '<th>Subtotal</th><th>Sales Tax</th><th>Occ Tax</th><th>Total</th></tr>')

    for guest_info in cust:
        f.write('<tr>')
        f.write('<td>' + guest_info[0] + '</td>' +
                '<td>' + guest_info[1] + '</td>' +
                '<td>' + str(guest_info[3]) + '</td>' +
                '<td>' + format(float(guest_info[4]), currency) + '</td>' +
                '<td>' + format(float(guest_info[5]), currency) + '</td>' +
                '<td>' + format(float(guest_info[6]), currency) + '</td>' +
                '<td>' + format(float(guest_info[7]), currency) + '</td></tr>')

    grand_total = sum(float(guest_info[7]) for guest_info in cust)
    f.write('<tr style="background-color: #87CEEB; color: #006400;">')
    f.write('<td colspan="3">Grand Total</td>' +
            '<td>' + format(grand_total, currency) + '</td>' +
            '<td colspan="3"></td></tr>')

    f.write('</table></center>\n')
    f.write('</body></html>')


############ call on main program to execute ############
main()
