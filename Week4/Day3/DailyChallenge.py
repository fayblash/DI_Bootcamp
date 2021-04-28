# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, the user entries the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

def encrypt(text,shift):
    cypher_text=""
    for letter in text:
        if (letter.isupper()):
            cypher_text += chr((ord(letter) + shift-65) % 26 + 65)
        elif (letter.islower()):
            cypher_text += chr((ord(letter) + shift-97) % 26 + 97)
        else:
            cypher_text += letter
    print(cypher_text) 
    
def decrypt(text,shift):
    cypher_text=""
    for letter in text:
        if (letter.isupper()):
            cypher_text += chr((ord(letter)-shift-65) % 26 + 65)
        elif (letter.islower()):
            cypher_text += chr((ord(letter)-shift-97) % 26 + 97)
        else:
            cypher_text+=letter
    print(cypher_text)
    
user_text=input("Enter a text for encryption/decryption: ")
enc_dec=input("Do you want to encrypt or decrypt? (enter e or d)? ")
shift=int(input("Enter the shift value for encryption: "))

if enc_dec=="d":
    decrypt(user_text,shift)
    
if enc_dec=="e":
    encrypt(user_text,shift)
      

