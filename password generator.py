import random
print("password generator")

chars =("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,1,2,3,4,5,6,7,8,9,0,!,@,#,$,*" )
number = input("Amount of passwords to generate : ")
number = int(number)
length = input("input your password length : ")
length = int(length)
print("here is your passwords : ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords+=random.choice(chars)


    print(passwords)    
