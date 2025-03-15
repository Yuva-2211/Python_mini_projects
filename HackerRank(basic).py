#Question 1
def Q1(a):
    list = a.split() # Spliting the sentence within their index
    reversed_list = list[::-1]
    reversed_a = ''.join(reversed_list) #joining the splited index and storing it in final variable
    return reversed_a.swapcase()

a = str(input())
print(Q1(a))
#Question 2
#Vending Machine :
'''class VendingMachine():
    def __init__(self,a,b):# intialising the Class
        self.a = a # no. of  items (present in machine)
        self.b = b #Price of items (present in machine)
    def buy(self , items , money ):#items = requirement of customer and money = provided by customer
        if (self.a>= items and items*self.b<=money):
            return money(items * b)
        else:c
            if(self.a<money):
                return "Not Enough Items"
            else:
                return "Not Enough Money"'''
            



