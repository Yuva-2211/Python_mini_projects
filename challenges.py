a = int(input("enter:"))
def fibi(a):
    if a == 0:
        return 0 
    elif a == 1:     
        return 1
    else:
        return fibi(a-1) + fibi(a-2)
for i in range(a):
    print(fibi(i))
