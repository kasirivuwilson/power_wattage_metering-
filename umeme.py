#make a heading or welcome message.
#from curses.ascii import isdigit
from turtle import pu


print('\t umeme self help'.upper())

#Request for an account no from the user.
account_number = input('Account No: ')

#Ask for the amount to pay from the user.
try:
    amount_to_pay = int(input('Amount to pay: '))

    class wattage:
        def wilson(self,amount):
            self.amount = amount
            amount_per_unit = 1100
            units = amount/amount_per_unit
            return round(units)
except:
    while (1):
        print('\n \t Enter amount in figures only!')
        amount_to_pay = int(input('Amount to pay: '))
        if (amount_to_pay.isdigit()):
            amount_to_pay = int(input('Amount to pay: '))
            class wattage:
                def wilson(self,amount):
                    self.amount = amount
                    amount_per_unit = 1100
                    units = amount/amount_per_unit
                    return round(units)
            break 

        print("you purchased {} units".format(wattage().wilson(amount_to_pay)))
class wattage:
    def wilson(self,amount):
        self.amount = amount
        amount_per_unit = 1100
        units = amount/amount_per_unit
        return round(units)


#Generate a random token to correspond to the purchased wattage.

#wattage(amount_to_pay) 


#Display the token to the user.
#Display the current user balance.
#Display the purchased wattage and its cost.
print("you purchased {} units".format(wattage().wilson(amount_to_pay)))

