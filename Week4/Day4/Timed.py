# Count Occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.
def char_count(string,letter):
    count=string.count(letter)
    print(f"'{letter}' appears in '{string}' {count} times.")

def main():
    string=input("Enter a sentence: ")
    letter=input("Enter a letter: ")
    char_count(string,letter)
# String: Programming is cool!
# Character: o
# 3
main()

# String: This is a great example
# Character: y
# 0