# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
class Circle():
    all_circles=[]
    def __init__(self,radius):
        self.radius=radius
        self.diameter=radius*2
        self.area=radius**2*3.14
        self.all_circles.append(self.area)
# Other abilities of a Circle instance:
    def change(self,value,word):
        self.all_circles.remove(self.area)
        if word=="radius":
            self.radius=value
            self.diameter=value*2
            self.area=value**2*3.14
        elif word=="diameter":
            self.diameter=value
            self.radius=value/2
            self.area=(value/2)**2*3.14
        else:
            print("Invalid Data")
        self.all_circles.append(self.area)    
# Compute the circle’s area
    def get_area(self):
        area=self.radius**2 * 3.14
        self.area=area
        return area
# Print the circle and get something nice
    def __str__(self):
        return f"This circle has an area of {self.area}. Circles are the greatest thing ever!!"
    
    def __int__(self):
        return self.area
# Be able to add two circles together
    def __add__(self,other):
        return self.area+other.area
        
# Be able to compare two circles to see which is bigger
    def __gt__(self,other):
        if self.area>other.area:
            return True
        else:
            return False
# Be able to compare two circles and see if there are equal
    def __eq__(self,other):
        if self.area==other.area:
            return True
        else:
            return False
# Be able to put them in a list and sort them
    def printall(self):
        print(sorted(self.all_circles))
        
c1=Circle(4)
c2=Circle(10)
print(c1)
print(c1>c2)
c1.printall()
c2.change(50,"diameter")
print(c2)
c1.printall()
