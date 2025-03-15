'''Rent calculator 
conditions :
*calculate rent for given amount of days
*calculate current bill
give user the both rent and current bill
'''

days=int(input("enter the no of days you stayed:"))
agreement = float(input("enter the rent per month:"))

factor = agreement/30

finalrent = days*factor

units = float(input("how many units did you burnt 😃 :")) 
print("ohh is it ",units)
pricefactor = float(input("whats the price of one unit in your place:",))
servicecharge = 90
fixedcharges = 19

currentbill=units*pricefactor+servicecharge+fixedcharges


doyouneedtotalamount=str(input('do you need total amount yes or no:'))
if(doyouneedtotalamount == "yes"):
    print(currentbill+finalrent)
else:
    print("you are rent is",finalrent ,"and your current bill =",currentbill)


print("Be a good tenet and pay your bills 😃\nThanks for using\nHave a good timetime 😄!!")



 