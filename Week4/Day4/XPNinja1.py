# Exercise 1 : Box Of Stars
# Instructions
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************
def star_maker():
    user_input = input("Please enter several words separated by commas (no spaces): ");
    list_input = user_input.split(',')
    # checking for length of longest word
    longest = 0;
    for item in list_input:
        if len(item)>longest:
            longest = len(item)
        
    # //print star box
    print("*"*(longest+4))
    for item in list_input:
        print("* "+item+" "*(longest-len(item))+" *")
    print("*"*(longest+4))
    
star_maker()

# Exercise 2
# Analyse this code before executing it. What is the purpose of this code? sorts in from lowest to highest
def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)
