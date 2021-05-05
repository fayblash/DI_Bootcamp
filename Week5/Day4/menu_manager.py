# Create a file called menu_manager.py. The file should contain a class called MenuManager, with the following functions:
import json
 
class MenuManager():
    
# __init__() - The function should attempt to read the menu from its file path (hard-coded inside the class) and store it in a variable called menu.
    def __init__(self):
        with open("menu.json", 'r') as f:
            self.menu = json.load(f)
# add_item(name, price) – this method should add an item to the menu, although do not save the changes to the file yet.
    def add_item(self,name,price):
        self.menu.append({"name":name,"price":price})        
# remove_item(name) – if the item is in the menu, this function should remove it from the menu (and again do not save the changes to the file yet) and return True. If the item was not in the menu, return False. (Hint: use Python’s del operator).
    def remove_item(self,name):
        self.menu=[i for i in self.menu if not (i["name"]==name)]
# save_to_file() - try and save the menu to the file it was loaded from in the __init__() method.
    def save_to_file(self):
        with open("menu.json", 'w') as f:
            json.dump(self.menu, f, indent = 2, sort_keys=True)

# Create a file called menu_editor.py , which will have the following functions:
# load_manager()- this function should create a new MenuManager instance.
def load_manager():
    return MenuManager()
# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to choose an item. Call the appropriate function that matches the user’s input.
def show_user_menu(object):
    flag=True
    while flag:
        choice=input('''
        MENU
(a) Add an Item
(d) Delete an Item
(v) View the Menu
(x) Exit
    ''')
        if choice=="a":
            add_item_to_menu(object)
        elif choice=="d":
            remove_item_from_menu(object)
        elif choice=="v":
            show_restaurant_menu(object)
        elif choice=="x":
            flag=False
        else:
            raise Exception("invalid data entered")
            break
# add_item_to_menu() - this will ask the user to input the item’s name and price. It will not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
def add_item_to_menu(object):
    name=input("Enter the name of an item to add to the menu: ")
    price=int(input("Enter the price of the item: "))
    object.add_item(name,price)
    object.save_to_file()
# If the item was added successfully print a message telling the user that the item was added successfully.
    # print(object.menu)
# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. The function should not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
def remove_item_from_menu(object):
    name=input("Enter the name of the item you wish to delete")
    object.remove_item(name)
    object.save_to_file()
    # print(object.menu)
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.
# show_restaurant_menu() - print the restaurant’s menu.
def show_restaurant_menu(object):
    object.save_to_file()
    print(object.menu)
# When the user chooses to exit the program, first write the menu to the file and then print a message that states that the menu was saved, finally exit the program.

# After exiting the program the changes should be reflected in the menu (see Part 1.1) and in the JSON file.

# Here’s an example of the menu shown to the user:

# Exercise Menu Manager
new_manager=load_manager()
show_user_menu(new_manager)

