# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints some of python’s built-in functions such as abs(), int(), raw_input().
# Write a documentation for your newly created function.


# Exercise 2: Currencies
# Instructions
# Create the code which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
class Currency():
    def __init__(self,type,amount):
        self.type=type
        self.amount=amount
    
    def __str__(self):
        if self.amount>1:
            return f'{self.amount} {self.type}s'
        else:
            return f'{self.amount} {self.type}'
    
    def __repr__(self):
        if self.amount>1:
            return f'{self.amount} {self.type}s'
        else:
            return f'{self.amount} {self.type}'
    
    def __int__(self):
        return self.amount
    
    def __sub__(self, other):
        try:
            if self.type == other.type:
                return self.amount - other.amount
            else:
                return TypeError("You can't subtract 2 different currencies")
        except:
            return self.type - other
        
    # def __add__(self, other):
    #     if isinstance(other,Currency):
    #         if self.type == other.type:
    #             return self.amount + other.amount
    #         else:
    #             return ValueError
    #     elif isinstance (other,int):
    #         return self.amount + other
    #     else:
    #         return ValueError
    def __add__(self, other):
        try:
            if self.type == other.type:
                return self.amount + other.amount
            else:
                return TypeError("You can't add 2 different currencies")
        except:
            return self.amount + other
        
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c4 = Currency('shekel', 1)
c3 = Currency('shekel', 10)    

print(str(c1))
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15
print(c2+c4)
# >>> c1 
# 5 dollars

# c1 += 5
# print(c1)
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


