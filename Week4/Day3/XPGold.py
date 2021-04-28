# # Exercise 1: Birthday Look-Up
# # Instructions
# # Create a variable called birthdays. Its value should be a dictionary.
# # Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# # Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# # Ask the user to give you a person’s name and store the answer in a variable.
# # Get the birthday of the name provided by the user.
# # Print out the birthday with a nicely-formatted message.
# birthdays={"Fay":"1981/01/22","Elisheva":"2002/07/21","Ezra":"2004/03/25","Elazar":"2008/04/03","Noam":"2010/01/21","Tali":"2012/04/29","Nava":"2016/08/04"}
# print("Welcome! You can look up the birthdays of the people in the list.")
# name=input("Enter a person's name and I'll tell you their birthday if they're in my list: ")
# if name in birthdays:
#     print(f"{name}'s birthday is {birthdays[name]}")
# else:
#     print("I don't know their birthday")

# # Exercise 2: Birthdays Advanced
# # Instructions
# # Before asking the user to input a person’s name print out all of the names in the dictionary.
# # If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)
# # keysList = list(birthdays.keys())
# print("The names in my database are: ")
# print(', '.join(list(birthdays.keys())))


# # Exercise 3: Add Your Own Birthday
# # Instructions
# # Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# # Ask the user for a person’s name – store it in a variable.
# # Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# # Now add this new data into your dictionary.
# # Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.
# name=input("Enter your name: ")
# dob=input("Enter your birthday (YYYY/MM/DD): ")
# birthdays[name]=dob
# # Exercise 4: Fruit Shop
# # Instructions
# # Create a new dictionary called items and populate the dictionary with the following key value pairs, each pair represents an item and its price.
# items= {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# # Print all the items and their prices in a sentence.
# for k,v in items.items():
#     print(f"We have {k}s which cost ${v} each.")
# # Change the value of all the keys to dictionaries containing both the price and the amount of items in stock.
# import random

# for k,v in items.items():
#     random_number = random.randint(1, 10)
#     items[k]={v:random_number}
# print(items)
# # Once you’ve added the stock details write some code to calculate how much it would cost to buy everything in stock.
# sum=0
# temp_sum=0
# for fruit,cost in items.items():
#     for stock in cost:
#         temp_sum= stock*cost[stock]
#         print(f"The total cost of {cost[stock]} {fruit}s is ${temp_sum}.")
#     sum+=temp_sum    
# print(f"The total cost of everything is ${sum}.")    
    

# Exercise 5 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
carstring = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
# Convert it into a list using Python (don’t do it by hand!).
carlist = carstring.split(", ")
print(carlist)
# Print out a message saying how many manufacturers/companies are in the list.
print(f"They're are {len(carlist)} manufacturers in the list")
# Print the list of manufacturers in reverse/descending order (Z-A).
print(sorted(carlist))
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
total=0
for car in carlist:
    if "o" in car:
        total+=1
print(f"There are {total} names with the letter 'o' in the list.")
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.
total2=0
for car in carlist:
    if "i" not in car:
        total2+=1
print(f"There are {total2} names in the list that don't have the letter 'i' in them.")
# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
duplicate=["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
print(duplicate)
# Remove these programmatically. (Hint: you can use sets to help you).
duplicate=set(duplicate)
print(duplicate)
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
dupstring=', '.join(duplicate)
print(f"The companies are: {dupstring}.")
print(f"There are {len(duplicate)} companies.")
# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
sortcar=sorted(duplicate)
for car in sortcar:
    print(car[::-1])

