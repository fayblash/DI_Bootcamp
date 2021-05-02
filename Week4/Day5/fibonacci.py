def fib(number):
    prev=0
    temp=0
    fibnum=1
    fibarr=[0]
    for i in range(number):
        fibarr.append(fibnum)
        temp=fibnum
        fibnum+=prev
        prev=temp
    return fibarr
x=fib(20)
print(x)
