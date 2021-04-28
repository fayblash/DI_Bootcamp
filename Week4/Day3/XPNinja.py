# # Exercise 1: List Of Integers - Randoms
# # Instructions
# # Continuation of the Exercise 2 XP NINJA - from Week4Day2

# # Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
# import random
# # i=0
# # list=[]
# # while i<10:
# #     list.append(random.randint(-100, 100))
# #     i+=1   
# # print(list) 
# # Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# listlen = random.randint(1, 50)
# i=0
# list=[]
# while i<listlen:
#     list.append(random.randint(-100, 100))
#     i+=1   
# print(list) 
# # Will the code work when the number of random numbers is not equal to 10?

# # list= [3, 47, 99, -80, 22, 97, 54, -23, 5, 47] 
# # #     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
# # #     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
# # #     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# # Store the list of numbers in a variable.
# # Print the following information:
# # a. The list of numbers – printed in a single line
# print(*list, sep=', ')
# # b. The list of numbers – sorted in descending order (largest to smallest)
# list.sort(reverse = True)  
# print(list) 
# # c. The sum of all the numbers
# print(sum(list))
# # A list containing the first and the last numbers.
# firstlast=[]
# firstlast.append(list[0])
# firstlast.append(list[-1])
# print(firstlast)
# # A list of all the numbers greater than 50.
# greater=[]
# for num in list:
#     if num>50:
#         greater.append(num)
# print(greater)
# # A list of all the numbers smaller than 10.
# smaller=[]
# for num in list:
#     if num<10:
#         smaller.append(num)
# print(smaller)
# # A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# squared=[]
# for num in list:
#     sq=num**2
#     squared.append(sq)
# print(squared)
# # The numbers without any duplicates – also print how many numbers are in the new list.
# list = sorted(set(list))
# print(list)
# print(len(list))
# # The average of all the numbers.
# avg = sum(list)/len(list)
# print("The average is ", round(avg,2))
# # The largest number.
# print(max(list))
# # 10.The smallest number.
# print(min(list))

# Exercise 2: Authentication CLI - Login:
# Instructions
# Create a dictionary that contains users: each key will represent a username, and each value will represent that user’s password. Initialize this dictionary with 3 users & passwords.
users={
    "fay123":"secretpw",
    "shev789":"reallysecretpw",
    "ezra456":"obviouspw"
}
# Create a loop that does the following:
# If the user inputs “exit”, break out of the loop.
loggedin=[]
userinput=input("Do you want to login or exit? ")
if userinput=="login":
    name=input("Enter your username: ")
    if (name) in users.keys():
        pw=input("Enter your password: ")
        if users[name]==pw:
            print("You are now logged in.")
            loggedin.append(name)
        else:
            print("Incorrect password")
    else:
        signup=input("Would you like to sign up? (y/n)")
        if signup=="y":
            name=input("Create a username: ")
            if name in users:
                    

# If the user inputs “login”, ask them for their username and password.
# If the user’s details exist print “you are now logged in”.
# If the user is successfully logged in, store the username in a variable called logged_in so we can track it later.


# Exercise 3: Authentication CLI - Signup:
# Instructions
# Continuation of the Exercise Above - Authentication CLI - login

# If the user does not exist ask if they would like to sign up:
# Ask the user for a username and make sure it doesn’t exist as a key in our dictionary, if the username is not valid continue asking the user to input a username.
# Ask the user for a password. The password is the value.
