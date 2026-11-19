def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+(n-2)
n=int(input("enter the num"))
for i in range(n):
    print(fibo(n))