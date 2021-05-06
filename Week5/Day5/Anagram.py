# First Download this text file : right click –> Save As

# Create a new file called anagram_checker.py which contains a class called AnagramChecker.
class AnagramChecker():
    def __init__(self):
        with open("wordlist.txt") as f:
            self.word_list=[word.strip() for word in f]
        self.results={}
# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.
                
    def get_word(self):
        flag=True
        while flag:
            word=input("Please enter a word and I'll tell you its anagrams: ").upper()
            print(word)
            if word in self.word_list:
                self.results[word]=[]
                return word
            else:
                print("This is not a real word. Try again.")
            
# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)
    def get_anagrams(self,word1):
        for word2 in self.word_list:
            self.is_anagram(word1,word2)
                
        
# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
    def is_anagram(self,word1,word2):
        w1_list = list(word1)
        w1_list.sort()
        w2_list = list(word2)
        w2_list.sort()
        if (w1_list == w2_list):
            self.results[word1].append(word2)
            
    
# Note: None of the methods in the class should print anything.
    def play(self):
        self.get_anagrams(self.get_word().upper())
        
# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
def main():
    new_anagram=AnagramChecker()
    show_menu(new_anagram)
    
    
def show_menu(object):
    flag=True
    while flag:
        menu_choice=input('''
Menu:
(p) Play the Anagram game
(x) Exit  ''').lower()
        if menu_choice=="p":
            object.play()
        elif menu_choice=="x":
            print_results(object)
            flag=False
        else:
            print ("Invalid entry. Try again. ")

def print_results(object):
    print("The anagrams we found today were: \n")
    for k,v in object.results.items():
        print(f"{k}:{v}") 

main()
# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.