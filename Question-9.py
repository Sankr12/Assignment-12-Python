print()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
M = num1
N = num2
i = 2
a = 1 

while i <= max(num1,num2):
    if num1 % i == 0 and num2 % i == 0:
        a = a * i
        num1 = num1//i
        num2 = num2//i
    elif num1 % i != 0 and num2 % i == 0:
        a = a * i
        num2 = num2//i
    elif num1 % i == 0 and num2 % i != 0:
        a = a * i
        num1 = num1//i
    else:
        i += 1

print()
print("LCM of", M, "and", N, "is", a)
print()
