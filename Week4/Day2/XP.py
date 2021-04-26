# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
my_fav_numbers = {7, 1, 100, 40}
my_fav_numbers.update([21, 99])
my_fav_numbers.pop()
friend_fav_numbers = {34, 43, 56}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
int_tuple = (7,8,9)
# tuples are immutable, can't add to them

# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
for x in range(1, 21):
    print(x)

# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
list_float = []
for i in range(3, 11, 1):
    list_float.append(i / 2.0)
print(list_float)

# Exercise 5: Shopping List
# Instructions
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
basket.count("Apples")
basket.clear()
print(basket)

# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
my_name="fay"
user_name=""
while user_name != my_name:
    user_name=input("Is your name the same as mine? Enter your name:")

# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.
shopping_list = ["milk", "eggs", "chicken", "cauliflour", "tomatoes", "apples", "pears"]
for i in range(0,len(shopping_list),2):
    print(shopping_list[i])

for index, item in enumerate(shopping_list):
    if index%2==0:
        print(item)
# Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1500,2501,1):
    if i%5==0 or i%7==0:
        print(i)
        
# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
fruit_input=input("Enter your favorite fruit(s), multiple entries separated by a space: ")
fruit_list=fruit_input.split(" ")
print(fruit_input)
print(fruit_list)

# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
pizza_toppings =[]
topping=""
while topping != "quit":
    topping = input("What toppings do you want on your pizza? Enter quit when you're finished: ")
    if topping == "quit":
        break
    else:
        pizza_toppings.append(topping)
print('Your toppings are:')
for top in pizza_toppings:
    print(top)
cost = 10 + (len(pizza_toppings)*2.5)
print(f"Your total cost is ${cost}.")

# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.
family_ages =[]
age_input="0"
while age_input != "quit":
    age_input = input("Enter the age of each ticket buyer? Enter quit when you're finished: ")
    if age_input == "quit":
        break
    else:
        family_ages.append(age_input)
total_cost=0
for age in family_ages:
    if int(age)<3:
        total_cost+=0
    elif int(age)<12:
        total_cost+=10
    else:
        total_cost+=15
print(f"Your total cost is ${total_cost} for {len(family_ages)} tickets.")

names = ["Fay","Elisheva","Ezra","Elazar","Noam","Tali","Nava"]
old_enough=[]
for name in names:
    age=input(f"How old is {name}?")
    if 21>int(age)>16:
        old_enough.append(name)
print("The following people may watch the movie: ")
for person in old_enough:
    print(person)

# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
# At the end, print the final list.
names = ["Fay","Elisheva","Ezra","Elazar","Noam","Tali","Nava"]
old_enough=[]
for name in names:
    age=input(f"How old is {name}?")
    if int(age)>16:
        old_enough.append(name)
print(old_enough)

# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders=["pb&j","grilled cheese","egg & cheese","turkey"]
finished_sandwiches=[]
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
sandwich_orders=["pb&j","pastrami","grilled cheese","pastrami","egg & cheese","pastrami","turkey"]
print("Sorry, we're out of pastrami.")
updated_list=[]
for sandwich in sandwich_orders:
    if sandwich != "pastrami":
        updated_list.append(sandwich)
finished_sandwiches=[]
for item in updated_list:
    print(f"I made your {item} sandwich.")
    finished_sandwiches.append(item)
