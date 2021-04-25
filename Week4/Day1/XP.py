print('Hello World\n'*4)

print((99**3)*8)

# 5 < 3 false
# 3 == 3 true
# 3 == "3" false
# "3" > 3 can't compare int and string
# "Hello" == "hello" false

computer_brand = 'Dell'
print(f'I have a {computer_brand} computer')

name='Fay'
age='40'
shoe_size=41
info = f'Hi my name is {name} and I am {age} years old, and I wear a size {shoe_size} in shoes.'
print(info)

a=20
b=30
if a>b:
    print('Hello World')

number=input("Enter a number and I'll tell you if it's odd or even: ")
if int(number)%2==0:
    print("Even")
else:
    print("Odd")

myname="fay"
yourname=input("Enter your name: ")
if myname==yourname.lower():
    print("Cool! We have the same name!")
else:
    print("My name is cooler than yours.")

inch=float(input("Enter your height in inches: "))
cm = inch * 2.54
# print(cm)
if cm > 145:
    print("You are tall enough to go on the ride!")
else:
    print("You need to grow some more to go on the ride.")