import random

string = input("Enter a string of 10 letters: ")
if len(string) < 10:
    print("Your string is not long enough")
elif (len(string)>10):
    print("Your string is too long")
else:
    print(string[0]+string[-1])
    letter=""
    for s in string:
        letter+=s
        print(letter)

    shuffled=''.join(random.sample(string,len(string)))
    print(shuffled)

    l = list(string)
    random.shuffle(l)
    result = ''.join(l)
    print(result)


