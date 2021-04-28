# Exercise 1 : What’s Your Name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.
def get_full_name(**names):
    name=""
    for value in names.values():
        name+=value +" "
    print(name)  

get_full_name(first="Fay",last="Blashka")
get_full_name(first="Elisheva",middle="Leah",last="Gersten")    


# Exercise 2 : From English To Morse
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
morse_dict = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def to_morse(string):
    morse=""
    stringlist=string.split(" ")
    for word in stringlist:
        for char in word:
            if char.upper() in morse_dict:
                morse+=morse_dict[char.upper()]+" "
        morse+="/"   
    print(morse) 

def from_morse(morse):
    sentence=""
    morselist=morse.split(" /")
    for word in morselist:
        morseword=word.split(" ")
        for word in morseword:
            if word in morse_dict.values():
                key = [k for k, v in morse_dict.items() if v == word][0]
                sentence+=key    
        sentence+=" "
    print(sentence)

main():
    en_dec=input("Do you want to encrypt to Morse code or decrypt from Morse code(e/d): ").tolower()
    userinput=input("Enter a text to convert: ")
    if en_dec=="e":
        to_morse(userinput)
    elif en_dec=="d":
        from_morse(userinput)
    else:
        print("Invalid data")
        
to_morse("I love you")
from_morse(".. /.-.. --- ...- . /-.-- --- ..-")