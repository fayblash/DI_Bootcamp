# Exercise 1: Temperature Advice
# Instructions
# Create a function called get_random_temp().
from random import randint

# def get_random_temp():
#     temp=randint(-10,40)
#     return temp
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
def main():
    temp=get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")    
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
    if temp<0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
    elif temp<16:
        print("Quite chilly! Don’t forget your coat")
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
    elif temp<23:
        print("A bit chilly, take a sweatshirt")
# between 16 and 23
    elif temp<32:
        print("It's a gorgeous warm day outside!")
# between 24 and 32
    elif temp<40:
        print("It's hot! take a water bottle and hat with you!")
# between 32 and 40
    else:
        print("It's a scorcher!Don't go out if you don't have to!")

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
def get_random_temp(season):
    if season=="winter":
        temp=randint(-10,16)
    elif season=="spring":
        temp=randint(17,23)
    elif season=="summer":
        temp=randint(24,40)
    elif season=="fall":
        temp=randint(14,20)
    else:
        temp=20
    return temp
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
season=input("Enter a season: (summer,spring,winter,fall): ")
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
get_random_temp(season)
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
round(random.uniform(-10,40), 2)
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
def get_random_temp(season):
    if 12<=season<=2:
        temp=randint(-10,16)
    elif:3<= season<=5:
        temp=randint(17,23)
    elif 6<=season<=8:
        temp=randint(24,40)
    elif 9<=season<=11:
        temp=randint(14,20)
    else:
        temp=20
    return temp

season=int(input("Enter a month: (1 for January, 2 for February,etc.): "))
get_random_temp(season)