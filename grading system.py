''' Grading system which gives respective grades to their marks!!!
 '''

marks = int(input("enter your marks :"))
if(marks >= 90):
    print('Grade A')
elif(marks <90 and marks >=80 ):
    print('Grade B+')
elif(marks <80 and marks >= 75):
    print('Grade B')
elif(marks <75 and marks >=65):
    print('Grade C')
elif(marks <65 and marks >= 35):
    print('Pass')
else:
    print("Fail , try hard next time ")