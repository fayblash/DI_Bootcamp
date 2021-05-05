import random
# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.
# words=[]
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
# def get_words_from_file(file):
#     with open(file,mode="r") as f:
#         wordstring=f.read()
#         list=[word for word in wordstring.split("\n")]
#         f.close()
#         return list
    
def get_words_from_file(file):
    with open(file, 'r') as f:
        return [word[:-2] for word in f]

    
words=get_words_from_file("wordlist.txt")

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
def get_random_sentence(number):
    sentence=""
    for i in range(number):
        sentence+=random.choice(words).lower()+" "
    return sentence
# Take the random words and create a sentence (using a python method), the sentence should be lower case.
def main():
    number=int(input("Enter a number and I'll make you a random sentence that length: "))
    if not type(number) is int:
      raise TypeError("Only integers are allowed")
    randsent=get_random_sentence(number)
    print(randsent)   

main()
# # Create a function called main which will:
# # Print a message explaining what the program does.

# # Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

# Exercise 2: Working With JSON
# Instructions
import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
json_file = 'sample.json'
with open(json_file, 'r') as file_obj:
    emp_data = json.load(file_obj)

print(emp_data["company"]["employee"]["payable"]["salary"])
emp_data["company"]["employee"]["birth_date"]="22/01/1981"
print(emp_data["company"]["employee"]["birth_date"])

with open(json_file, 'w') as file_obj:
    json.dump(emp_data, file_obj,indent = 2, sort_keys=True)
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
