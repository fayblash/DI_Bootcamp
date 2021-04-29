# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.
def insert_at(list,index,item):
    list.insert(index,item)

# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.
def spaces(string):
    return string.count(" ")

# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.
def upperlower(string):
    upper = 0
    lower=0
    for letter in string:
        if letter.isupper():
            upper+=1
        elif letter.islower():
            lower+=1
        else:
            continue
    return (upper,lower)  

x = upperlower("You are so beautiful") 
print(x) 
# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:
def sum_array(list):
    sum=0
    for num in list:
        sum+=num
    return sum
#     >>>my_sum([1,5,4,2])
#     >>>12

# Exercise 5
# Instructions
# Write a function to find the max number in a list

#     >>>find_max([0,1,3,50])
#     >>>50
def find_max(list):
    max=0
    for num in list:
        if num>max:
            max=num
    return max

# Exercise 6
# Instructions
# Write a function that returns factorial of a number
def factorial(num):
    i=1
    fact=1
    while i<=num:
        fact*=i
        i+=1
    return fact
# >>>factorial(4)
#     >>>24
y=factorial(4)
print(y)


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

#     >>>list_count(['a','a','t','o'],'a')
#     >>>2
def count_el(list,letter):
    count=0
    for i in list:
        if i==letter:
            count+=1
    return count
# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>norm([1,2,2])
#     >>>3


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

#     >>>is_mono([7,6,5,5,2,0])
#     >>>True
def is_mono(list):
    if list == sorted(list) or list==sorted(list, reverse=True):
        return True
    else:
        return False

print(is_mono([7,6,5,5,2,0]))  
print(is_mono([2,3,3,3]))      
print(is_mono([1,2,0,4]))      
#     >>>is_mono([2,3,3,3])
#     >>>True

#     >>>is_mono([1,2,0,4])
#     >>>False


# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.
def longest_word(list):
    longest_string = max(list, key=len)
    return longest_string

list=["sdfsdd","asfhwgukfygeyg","fhfgg","sduhriuhgisurhgiher"]
print(longest_word(list))
# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.


# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

#     >>>is_palindrome('radar')
#     >>>True

#     >>>is_palindrome('John)
#     >>>False


# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

#     >>>common_div(10,20)
#     >>>[2,5,10]


# Exercise 16
# Instructions
# Write a function that test if a number is prime:
def is_prime(num):
    if 
#     >>>is_prime(11)
#     >>>True


# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]
def weird_print(list):
    newlist=[num for i,num in enumerate(list) if i==num]
    return newlist
print(weird_print([1,2,2,8,4,9]))
# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2
# def type_count(**kwargs):
#     for item in **kwargs:
        
    

# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.


# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"
def make_pw(string):
    sentence=""
    for i in string:
        sentence+="*"
    return sentence

print(make_pw("asdfgh"))

