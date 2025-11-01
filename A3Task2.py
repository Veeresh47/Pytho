import math
def calculate(num):
    r1=math.sqrt(num)
    r2=math.log(num)
    r3=math.sin(num)
    return r1,r2,r3


n=int(input("Enter a number:"))
R1,R2,R3=calculate(n)
print("Squre root : ",R1)
print("Logarithm : ",R2)
print("Sine :",R3)