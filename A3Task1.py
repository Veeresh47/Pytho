def fact(num):
    if num==1:
        return 1
    else:
        factorial=num*fact(num-1)
        return factorial

n=int(input("enter a number:"))
r=fact(n)
print(f"Factorial of {n} is : {r}")