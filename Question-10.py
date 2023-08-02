# Write a python script to calculate HCF of two numbers

print()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    count = num1
else:
    count = num2
m=num1
n=num2    
i=2
a=1

while i<=count:
    if num1 % i == 0 and num2 % i == 0:
        a = a * i
        num1 = num1//i
        num2 = num2//i
    elif num1 % i != 0 and num2 % i == 0:
        num2 = num2//i
    elif num1 % i == 0 and num2 % i != 0:
        num1 = num1//i
    else:
        i=i+1

print()
print("HCF of",m,"and",n,"=",a)
print()
    
        

