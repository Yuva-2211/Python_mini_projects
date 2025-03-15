'''so we are going to convert the fahrenheit to celsius and vice versa'''

print("\n Choose the following functions to continue!!!") 
print("1.Fahrenheit to Celsius")
print("2.Celsius to Fahrenheit")
print("3.Exit")

a = int(input('Enter your choice:'))
while(a!=3):
  if(a==1):
    f=float(input("Enter in Fahrenheit:"))
    fac1 = (f-32)*5/9
    print(fac1, 'celsius')
    a = int(input('Enter your choice:'))
  elif(a==2):
    c = float(input("Enter in Celsius:"))
    fac2 = (9/5)*c+32
    print(fac2,'Fahrenheit')
    a = int(input('Enter your choice:'))
  continue
if(a==3):
  print("Bye!!, see you again")
else:
  print('invalid input')
             