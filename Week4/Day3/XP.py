# # Exercise 1 : Convert Lists Into Dictionaries
# # Instructions
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# # Expected output:
# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# newdict=dict(zip(keys, values))
# print(newdict)

# # Exercise 2 : Cinemax #2
# # Instructions
# # “Continuation of Exercise Cinemax from Week4Day2 XP”

# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.

# # Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# # How much does each family member have to pay ?
# total_cost=0
# for value in family.values():
#     if value<3:
#         total_cost+=0
#     elif value<12:
#         total_cost+=10
#     else:
#         total_cost+=15
# print(f"Your total cost is ${total_cost} for {len(family)} tickets.")

# # Print out the family’s total cost for the movies.
# # Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
# family={}
# member=""
# while member != "quit":
#     member = input("Enter the name and age of each ticket buyer (name,age)? Enter quit when you're finished: ")
#     if member == "quit":
#         break
#     else:
#         member=member.split(",")
#         family[member[0]]=int(member[1])
#         # family=dict(member)

# # Exercise 3: Zara
# # Instructions
# # Here is some information about a brand.
# brand={
# "name": "Zara", 
# "creation_date": 1975, 
# "creator_name": "Amancio Ortega Gaona",
# "type_of_clothes": ["men", "women", "children", "home"], 
# "international_competitors": ["Gap", "H&M", "Benetton"], 
# "number_stores": 7000, 
# "major_color": {
#     "France": "blue", 
#     "Spain": "red", 
#     "US": ["pink", "green"]}
# }
# # 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# # 3. Change the number of stores to 2.
# brand["number_stores"]=2
# # 4. Print a sentence that explains who Zaras clients are.
# print("Zara's clients are mainly:") 
# print(*brand['type_of_clothes'][:-1],sep = ', ')
# # 5. Add a key called country_creation with a value of Spain.
# brand["country_creation"]="Spain"
# # 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigua")
# # 7. Delete the information about the date of creation.
# del brand["creation_date"]
# # 8. Print the last international competitor.
# print(brand["international_competitors"][-1])
# # 9. Print the major clothes colors in the US.
# print(brand["major_color"]["US"])
# # 10. Print the amount of key value pairs (ie. length of the dictionary).
# print(len(brand))
# # 11. Print the keys of the dictionary.
# print(brand.keys())
# # 12. Create another dictionary called more_on_zara with the following details:
# more_on_zara={
# "creation_date": 1975, 
# "number_stores": 10000
# }
# # 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# brand.update(more_on_zara)
# print(brand)
# # 14. Print the value of the key number_stores. What just happened ?
# print(brand["number_stores"])

# Exercise 4 : Disney Characters
# Instructions
# Use this list :

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# Analyse these results :

# #1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
disney_users_A={}
for index, user in enumerate(users):
    disney_users_A[user]= index
print(disney_users_A)
# #2/

# >>> print(disney_users_B)
disney_users_B=dict(enumerate(users))
print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 
# users.sort()
disney_users_C=dict(enumerate(sorted(users)))
print(disney_users_C)

disney_users_D={}
for index, user in enumerate(sorted(users)):
    disney_users_D[user]= index
print(disney_users_D)
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
disney_users_E={}
i=0
for user in users:
    disney_users_E[user]=i
    i+=1
print(disney_users_E)
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
disney_users_F={}
i=0
for user in users:
    disney_users_F[i]=user
    i+=1
print(disney_users_F)
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
disney_users_A={}
for index, user in enumerate(users):
    if "i" in user:
        disney_users_A[user]= index
print(disney_users_A)

disney_users_E={}
i=0
for user in users:
    if "i" in user:
        disney_users_E[user]=i
        i+=1
print(disney_users_E)
# The characters, which names start with the letter “m” or “p”.

disney_users_E={}
i=0
for user in users:
    if user[0]()=="M" or user[0]=="P":
            disney_users_E[user]=i
            i+=1
print(disney_users_E)

