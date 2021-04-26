# Exercise 1 : Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.
list1=["happy","birthday"]
list2=["to","you"]
list1.extend(list2)
print(list1)

# Exercise 2: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87
i=0
numlist=[]
while i<3:
    numinput = int(input(f"Input number {i+1}: "))
    numlist.append(numinput)
    i+=1
print(numlist)
print(f"The greatest number is: {max(numlist)}")

# Exercise 3 : The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
import string 

alphabet_string = string.ascii_lowercase
vowels = ["a","e","i","o","u"]
for letter in alphabet_string:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant") 

# Exercise 4 :
# Instructions
# Using this variable
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
user_name = input("Please enter your name: ")

if user_name in names:
    print(names.index(user_name))
# Example: if input is 'Cortana' we should be printing the index 1


# Exercise 5 : Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
i=0
wordlist=[]
while i<7:
    wordinput = input(f"Input word {i+1}: ").lower()
    wordlist.append(wordinput)
    i+=1
print(wordlist)
letter = input("Enter a letter: ").lower()

for word in wordlist:
    if letter in word:
        print(f"{letter.upper()} appears in '{word}' at index {word.index(letter)}.")
    else:
        print(f"{letter.upper()} does not appear in '{word}'.")

# Exercise 6 :
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
i=1
numberlist=[]
while i<1000001:
    numberlist.append(i)
    i+=1
print(min(numberlist))
print(max(numberlist))
print(sum(numberlist))
# Exercise 7 :
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
numstring = input("Enter a sequence of numbers separated by commas: ")
numlist =numstring.split(",")
print(numlist)
numtuple=eval(numstring)
print(numtuple)

# Exercise 8 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.
import random
random_number = random.randint(1, 9)
usernum=input("Enter a number from 1 to 9 (inclusive): ")
if usernum == random_number:
    print("Winner!")
else:
    print("Better luck next time.")

#bonus
def play_the_game():
    print("Welcome to the guessing game!")
    play = "y"
    random_number = random.randint(1, 9)
    wincount=0
    losecount=0
    while play=="y":
        usernum=input("Enter a number from 1 to 9 (inclusive): ")
        if usernum == random_number:
            print("Winner!")
            wincount+=1
        else:
            print("Better luck next time.")
            losecount+=1
        play=input("Do you want to keep playing? (y/n)")
    # bonus2
    print(f"You won {wincount} times")
    print(f"You lost {losecount} times")
    
play_the_game() 


    


