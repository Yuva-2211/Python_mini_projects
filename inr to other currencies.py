#INR to Dollars , Pounds , Yen 
def inr_to_dollar(inr):
    dollar_final = 0.012*inr
    return  print(f'{inr} Rupees, equal to {dollar_final} Dollars')
def dollar_to_inr(dollar):
    inr_final = dollar*84
    return print(f'{dollar} Dollars, equal to {inr_final} Rupees')
def inr_to_pounds(inr):
    pounds_final = inr*0.0091
    return print(f'{inr} Rupees,equal to {pounds_final} Pounds')
def pounds_to_inr(pounds):
    inr_final = pounds*110
    return print(f'{pounds} Pound,equal to {inr_final} Rupees')
def inr_to_yen(inr):
    yen_final = inr*0.56
    return print(f'{inr} Rupees,equal to {yen_final} Yen')
def yen_to_inr(yen):
    inr_final = yen*1.78
    return print(f'{yen} Yen,equal to {inr_final} Rupees')

print("choose the following options to continue")
print('1.inr_to_dollar\n2.dollar_to_inr\n3.inr_to_pounds\n4.pounds_to_inr\n5.inr_to_yen\n6.yen_to_inr')
print('7.Exit')
while True:
    choice = int(input('enter your choice:'))
        
    if(choice==1):
        inr = float(input('enter in INR:'))
        print(inr_to_dollar(inr))
        continue
    elif(choice==2):
        dollar = float(input('enter in DOLLAR:'))
        print(dollar_to_inr(inr))
        continue
    elif(choice==3):
        pound = float(input('enter in Pounds:'))
        print(pounds_to_inr(pound))
        continue
    elif(choice==4):
        inr = float(input('enter in Inr:'))
        print(inr_to_pounds(inr))
        continue
    elif(choice==6):
        yen = float(input('enter in Yen:'))
        print(yen_to_inr(yen))
        continue
    elif(choice==5):
        inr = float(input('enter in INR:'))
        print(inr_to_yen(inr))
        continue
    elif(choice==7):
            print('thank you,see you again ,\nBYE!!!')


        

    


