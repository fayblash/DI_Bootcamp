# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python
print("Hello World\n"*4 +"I love python\n"*4)

# Exercise 2 : What Is The Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)
month=int(input("Enter a month(1 to 12: "))
if (1<=month<=12):
    if (3<= month <=5):
        print("That month is in Spring.")
    elif (6 <= month <=8):
        print("That month is in Summer.")
    elif (9 <= month <=11):
        print("That month is in Autumn.")
    else:
        print("That month is in Winter.")
else:
    print("Invalid data entered.")
