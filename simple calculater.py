''' simple calculator  which can do following functions 

* Addition , subtraction , multiplication , division   of two numbers   '''

import math

def sum(a,b):
    return a+b

def sub(a,b):
    if(a>b):
      return a-b
    else:
       return b-a 

def multiply(a,b):
   return a*b

def division(a,b):
   q=a/b
   r=a%b
   print("\nQuotient =",q)
   print("Remainder =",r)
   
print("\n Choose the following functions to continue!!!") 
print("\n \t1.Addition")
print("\n \t2.Subtraction")
print("\n \t3.Multiplication")
print("\n \t4.Division")

a =float(input("enter number 1:"))
b=float(input("enter number 2:"))
choice = int(input("enter your choice of operation:"))
if choice==1:
   print(a,"+",b,'=',sum(a,b))
elif choice==2:
   print(a,'-',b,'=',sub(a,b))
elif choice==3:
   print(a,'*',b,'=',multiply(a,b))
elif choice==4:
   print(division(a,b))
else:
   print("invalid input")
