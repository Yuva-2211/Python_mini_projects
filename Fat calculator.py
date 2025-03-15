#Fat Calculator
''' for calculation of BFP 
calculate bmi and use BFP factor'''

print("Welcome to the Body Fat percentage calculator\n *Choose the following options \n\t1.Do you know your BMI? , calculate BFP\n\t2.Don't Know Bmi , no problem lets calculate\n\t3.Exit ")


while True:
   a = int(input("Enter your choice: "))
   if(a==1):
    print("Chalo,let's calculate\nPlease enter your BMI ")
    bmi=float(input("Enter your Bmi:"))
    age=float(input('enter your current age :'))
    Bfp = (1.2*bmi)+(0.23*age)-5.4
    print("This is your BMI:",bmi, "\nThis is your Body Fat Percentage:",Bfp )

    continue
   elif(a==2):
     print("Lets calculate both BMI and BFP!!")
     Weight = float(input("Enter your weight in Kilograms:"))
     Height = float(input("Enter your height in centimeters:"))
     Height1=Height*0.01
     age = float(input("Enter your Age:"))
     bmi=(Weight/(Height1*Height1))
     Bfp = (1.2*bmi)+(0.23*age)-5.4
     print("This is your BMI:",bmi,"\nThis is your Body Fat Percentage:",Bfp )
     
     continue
   else:
     print("Bye , see you again")

    
