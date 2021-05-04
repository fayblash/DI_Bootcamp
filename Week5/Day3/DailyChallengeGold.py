users=[]
for i in range(5):
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    score=int(input("Enter your score: "))
    users.append((name,age,score))
print(users)
users.sort(key=lambda x: (x[0], x[1],x[2]))
print(users)