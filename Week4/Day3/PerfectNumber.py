x = int(input('Enter the Number:'))
sum=0
i=1
# while i < x:
while i <= x/2:
    if x%i==0:
        sum+=i 
    i+=1
if sum==x:
    print("True")
else:
    print("False")