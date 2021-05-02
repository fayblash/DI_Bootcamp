# # Exercise 1 : Geometry
# # Instructions
# # Write a class called Circle that receives a radius as an argument (default is 1.0).
# # Write two instance methods to compute perimeter and area.
# # Write a method that prints the geometrical definition of a circle.
# import math

# class Circle:
#     def __init__(self,radius=1.0):
#         self.radius=radius

#     def get_perimeter(self):
#         return round((2 * math.pi * self.radius),2)
    
#     def get_area(self):
#         return round(math.pi * (self.radius**2),2)
    
#     def print_def(self):
#         print("A circle is the set of all points in the plane that are a fixed distance (the radius) from a fixed point (the centre). Any interval joining a point on the circle to the centre is called a radius.")    

# circle1=Circle(4)
# print(circle1.get_area())
# print(circle1.get_perimeter())
# circle1.print_def()
# # Exercise 2 : Custom List Class
# # Instructions
# # Create a class called MyList, the class should receive a list of letters.
# # Add a method that returns the reversed list.
# # Add a method that returns the sorted list.
# # Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
# from random import randint

# class MyList:
#     def __init__(self,letters):
#         self.letters=letters
    
#     def reversed_list(self):
#         return(sorted(self.letters, reverse=True))
    
#     def sorted_list(self):
#         return(sorted(self.letters))
    
#     def random_list(self):
#         return [randint(0,50) for letter in self.letters]

# list1=MyList(["f","g","a","z","e","i"])
# print(list1.reversed_list())
# print(list1.sorted_list())
# print(list1.random_list())

# Exercise 3 : Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.
# Create a python file called menu_manager.py.
# Create a class called MenuManager.
class MenuManager:
# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).
    def __init__(self):
        self.all_menu_items=[]
      
# Here is a list of the dishes currently on the menu:

#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True

#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# The dishes provided above should be the value of the menu attribute.

# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.
    def add_item(self,name,price,spice,gluten):
        item={}
        item["name"]=name
        item["price"]=price
        item["spice_level"]=spice
        item["gluten_index"]=gluten
        self.all_menu_items.append(item)
        
# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.
    def update_item(self,name,price,spice,gluten):
        for item in self.all_menu_items:
            if item["name"]==name:
                item["price"]=price
                item["spice_level"]=spice
                item["gluten_index"]=gluten
                return
        print("This item is not currently in the menu.")
# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.
    def remove_item(self,name):
        for item in self.all_menu_items:
                self.all_menu_items=[item for item in self.all_menu_items if not (item["name"] == name)]
    
    def show_menu(self):
        for item in self.all_menu_items:
            for k,v in item.items():
                print(f"{k}:{v}")  

fays_restaurant=MenuManager()
fays_restaurant.add_item("Soup",10,"B",False)
fays_restaurant.add_item("Hamburger",15,"A",True)
fays_restaurant.add_item("Salad",12,"A",False)
fays_restaurant.add_item("French Fries",5,"C",False)
# fays_restaurant.show_menu()
fays_restaurant.update_item("Soup",8,"A",False)
fays_restaurant.show_menu()
fays_restaurant.remove_item("Salad")

