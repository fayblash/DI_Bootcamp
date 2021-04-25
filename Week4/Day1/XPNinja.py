# Exercise 1 : Use The Terminal
# Instructions
# Run this command in the terminal to open a python console:
# $ python3
# Hint: Replace python3 with python for Windows

# Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.
# PATH explanation can be found here.


# Exercise 2 : Alias
# Instructions
# Read about alias, and try to open a python console with the command:
# $ py


# Exercise 3 : Outputs
# Instructions
# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9 //true
#     >>> 3 == 3 == 3 //true
#     >>> bool(0) //true
#     >>> bool(5 == "5") //false
#     >>> bool(4 == 4) == bool("4" == "4") //true
#     >>> bool(bool(None)) //false
#     x = (1 == True) //true
#     y = (1 == False) //false
#     a = True + 4  //5
#     b = False + 10 //10

#     print("x is", x)// x is True
#     print("y is", y) //y is False
#     print("a:", a) //a:5
#     print("b:", b) //b:10


# Exercise 4 : How Many Characters In A Sentence ?
# Instructions
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamcolaboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velitesse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text)) 


# Exercise 5: Longest Word Without A Specific Character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

def play_the_game():
    play = "y"
    new_length = 0
    while play=="y":
        string = input("Enter the longest sentence you can think of without the letter 'a': ")
        if "a" in string:
            print("There is a letter 'a' in your sentence.")
        else:
            length = len(string)
            if length > new_length:
                print(f"You win! Your sentence was {length} characters long.")
                new_length=length
            else:
                print("Your last sentence was longer.")
        play=input("Do you want to keep playing? (y/n)")

play_the_game()