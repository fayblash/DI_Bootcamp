# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
from math import *
c=50
h=30
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:
numstring = input("Enter a few numbers separated by commas: ")
numlist =numstring.split(",")
output=[]
for num in numlist:
    num=int(num)
    x=(sqrt((2*c*num)/h))
    output.append(int(x))
print(output)
# 18,22,24


# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:

list= [3, 47, 99, -80, 22, 97, 54, -23, 5, 47] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.
# Print the following information:
# a. The list of numbers – printed in a single line
print(*list, sep=', ')
# b. The list of numbers – sorted in descending order (largest to smallest)
list.sort(reverse = True)  
print(list) 
# c. The sum of all the numbers
print(sum(list))
# A list containing the first and the last numbers.
firstlast=[]
firstlast.append(list[0])
firstlast.append(list[-1])
print(firstlast)
# A list of all the numbers greater than 50.
greater=[]
for num in list:
    if num>50:
        greater.append(num)
print(greater)
# A list of all the numbers smaller than 10.
smaller=[]
for num in list:
    if num<10:
        smaller.append(num)
print(smaller)
# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
squared=[]
for num in list:
    sq=num**2
    squared.append(sq)
print(squared)
# The numbers without any duplicates – also print how many numbers are in the new list.
list = sorted(set(list))
print(list)
print(len(list))
# The average of all the numbers.
avg = sum(list)/len(list)
print("The average is ", round(avg,2))
# The largest number.
print(max(list))
# 10.The smallest number.
print(min(list))

# 11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
#sum
total=0
for num in list:
    total+=num
print(total)
#average
avg = total/len(list)
print("The average is ", round(avg,2))
#largest
highest=0
for num in list:
    if num>highest:
        highest=num
print(highest)
#smallest
smallest=highest
for num in list:
    if num<smallest:
        smallest=num
print(smallest)
# 12.Extra bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100.
# Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
counter=1
while counter<11:
    num=input(f"Enter number {counter} (between -100 and 100): ")
    list.append(int(num))
    counter+=1

# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
par="It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters. ‘My dear Mr. Bennet,’ said his lady to him one day, ‘have you heard that Netherfield Park is let at last?’ Mr. Bennet replied that he had not. ‘But it is,’ returned she; ‘for Mrs. Long has just been here, and she told me all about it.’ Mr. Bennet made no answer. ‘Do you not want to know who has taken it?’ cried his wife impatiently. ‘YOU want to tell me, and I have no objection to hearing it.’This was invitation enough."
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
print(par)
print(f"This paragraph contains {len(par)} characters")
# How many sentences it contains.
sentence=par.split(".")
print(f"This paragraph contains {len(sentence)} sentences.")
# How many words it contains.
word=par.split(" ")
print(f"This paragraph contains {len(word)} words.")
# How many unique words it contains.
# uniqueword = list(set(word))
# print(f"This paragraph contains {len(uniqueword)} unique words.")
# Bonus: How many non-whitespace characters it contains.
nowhite=par.replace(" ", "")
print(len(nowhite))
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.


# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.
import collections
# Suppose the following input is supplied to the program:
text="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
textlist=text.split()
print(textlist)
wordfreq={}
for word in textlist:
    wordfreq[word]=textlist.count(word)

# sorts the keys in order
ordered = collections.OrderedDict(sorted(wordfreq.items()))

for k, v in ordered.items():
    print(f"{k}:{v}")
# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1
