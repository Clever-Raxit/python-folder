# these will take some input in numbers.
num1=float(input("Enter first number: "))

# these will take the required operator.
op=input("Enter operator: ")

# these will take the another number.
num2=float(input("Enter second number: "))

# main part of calculator which processes 
# on the basis of the given input 
# and give out put
 
if op =="+":
    print(num1+num2)
elif op =="-":
    print(num1-num2)
elif op =="*":
    print(num1*num2)
elif op =="/":
    print(num1/num2)
else:
    print("invailed operator")
