#Simple interest calculator
p=float(input("Enter the principal "))
t=float(input("Enter the time in years "))
T=float(input("Enter the time in months "))
if T>0:
    t=t+(T/12)


r=float(input("Enter the rate of interest "))
si=(p*t*r)/100
print("The simple interest is ",si)