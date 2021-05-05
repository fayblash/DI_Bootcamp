import json
# Exercise 1 : Restaurant Menu Manager
# Instructions
# Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.
menu=[]

def add_item_to_menu(name,price):
    menu.append({"name":name,"price":price})

def read_from_secrets(data):
    with open(secret.json,"r") as file_obj:
        return json.load(file_obj)
    
def write_to_secrets(data):
    with open("secret.json","w") as file_obj:
        json.dump(data, file_obj)

try:
    menu=read_from_secrets()
except json.decoder.JSONDecodeError:
    menu=[]

print(menu)

while True:
    name= input("What item to add to menu: ")
    if name == "quit":
        break
    price=int(input(f"How much does {name} cost: "))
    add_item_to_menu(name,price)

print(menu)
write_to_secrets(menu)
# The menu should be saved to a local file – the program should load the file when it begins and add the updated details to the file before exiting.

# The program should be written in two files – one which will deal with the UI (user interface), eg. showing the user menu and getting user input, etc.
# The second file will handle all other functionality such as adding/removing items from the menu, along with loading and saving the data to a JSON file.
# Separating the files is important – the file which deals with the UI functionality should not have any details about the menu file itself (encapsulation).

# The following code is the basic menu for a restaurant. You can make any changes you want.

# {
#     "items": [
#         {
#             "name": "Vegetable soup",
#             "price": 30
#         },
#         {
#             "name": "Hamburger",
#             "price": 44.9
#         },
#         {
#             "name": "Milkshake",
#             "price": 22.5
#         },
#         {
#             "name": "Artichoke",
#             "price": 18
#         },
#         {
#             "name": "Beef stew",
#             "price": 52.5
#         }
#     ]
# }


# Create a file called menu_manager.py. The file should contain a class called MenuManager, with the following functions:
# __init__() - The function should attempt to read the menu from its file path (hard-coded inside the class) and store it in a variable called menu.

# add_item(name, price) – this method should add an item to the menu, although do not save the changes to the file yet.

# remove_item(name) – if the item is in the menu, this function should remove it from the menu (and again do not save the changes to the file yet) and return True. If the item was not in the menu, return False. (Hint: use Python’s del operator).

# save_to_file() - try and save the menu to the file it was loaded from in the __init__() method.

# Create a file called menu_editor.py , which will have the following functions:
# load_manager()- this function should create a new MenuManager instance.

# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to choose an item. Call the appropriate function that matches the user’s input.

# add_item_to_menu() - this will ask the user to input the item’s name and price. It will not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
# If the item was added successfully print a message telling the user that the item was added successfully.

# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. The function should not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

# show_restaurant_menu() - print the restaurant’s menu.

# When the user chooses to exit the program, first write the menu to the file and then print a message that states that the menu was saved, finally exit the program.

# After exiting the program the changes should be reflected in the menu (see Part 1.1) and in the JSON file.

# Here’s an example of the menu shown to the user:

# Exercise Menu Manager



# Exercise 2 : Giphy API #1
# Instruction
# Hint: For this exercise, check the documentation of the Giphy API

# You will work with this part of the documention

# You will use this Gif URL: https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
# Explanation of the Gif URL

# q Request Paramater: Search query term or phrase. We are searching for “hilarious” gifs

# rating Request Paramater: Filters results by specified rating. We are searching for Level 1 gifs. Check out the ratings documentation

# api_key Request Paramater : GIPHY API Key. Our API KEY is hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
# Fetch the giphs from the Gif URL provided above.
# If the status code is 200 return the result as a JSON object.
# Use f-strings and variables to build the URL string we’re using for the fetch.
# Only return gifs which have a height bigger then 100.
# Return the length of the object you received in the previous question.
# Only return the first 10 gifs. Hint: In the Giphy Documentation, check out the relevant Request Parameters.


# Exercise 3 : Giphy API #2
# Instructions
# Hint: For this exercise, You will work with this part of the documention
# You will use this API KEY : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My

# Create a small Python program which asks the user for a term or phrase and returns all the relevant gifs. (Example: all the “hilarious” gifs)
# If the term or phrase doesn’t exist or if the user didn’t enter a correct term or phrase, return the trending gifs of the day and a message stating that you couldn’t find the requested term or phrase.
# Note from the documentation : GIPHY Trending returns a list of the most relevant and engaging content each and every day.
