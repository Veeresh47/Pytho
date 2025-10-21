num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
print("Enter the operaton you want to perform: ")
print(" + ,  - ,  * ,  / ")
operation=input("Enter operation: ")
if operation =='+':
    result=num1+num2
    print("The sum is: ",result)
elif operation =='-':
    result=num1-num2
    print("The difference is: ",result)
elif operation =='*':
    result=num1*num2
    print("The product is: ",result)
elif operation =='/':
    if num2!=0:
        result=num1/num2
        print("The quotient is: ",result)
    else:
        print("Error: Division by zero is not allowed.")

else:

    print("Invalid operation selected.")
