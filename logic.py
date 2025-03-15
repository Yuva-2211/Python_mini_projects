#fibiconni series
def fibi(a):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        return fibi(i-1)+fibi(i-2)
#pattern 1
def right_triangle(rows):
    rows = int(input("enter:"))
    for i in range(0,rows):
        for j in range(0,i+1):
            print("*",end=" ")
        print()

#pattern 2 
def left_triangle(rows):
    rows = int(input("enter:"))
    for j in range(1,rows+1):
        print("*"* j)
#pattern 3
def square(rows):
    rows = int(input("enter:"))
    for i in range(rows):
        for j in range(rows):
            print("*",end=" ")
        print()
#pattern 4
def hill(rows):
    for i in range(rows):
        for j in range(rows-i-1):
            print("",end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print()        


#pattern 5
def lef_numtri(rows):
    for i in range(1,rows+1):
        for j in  range(1,i+1):
            print(j,end=" ")
    print()        
lef_numtri(rows=5)




