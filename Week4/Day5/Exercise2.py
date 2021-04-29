# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****
space=2
star=1
i=0
while i<3:
    sentence=""
    sentence+=" "*space+"*"*star+" "*space
    print(sentence)
    i+=1
    star+=2
    space-=1

# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****
length=5
i=1
while i<=length:
    sentence=""
    sentence+=" "*(length-i)+"*"*i
    print(sentence)
    i+=1

# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
i=1
counter=5
while i<11:
    sentence=""
    if i<6:
        sentence+="*"*i
    else:
        sentence+=" "*(i-6)+"*"*counter
        counter-=1
    print(sentence)
    i+=1
# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1):
#     minimum = i
#     for j in range( i + 1, len(my_list)):
#         if(my_list[j] < my_list[minimum]):
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)