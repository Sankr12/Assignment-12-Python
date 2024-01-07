# Write a python script to check whether a given pair of numbers are co-prime or not

print()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(2,min(num1,num2)):
    if num1%i==0 and num2%i==0:
        print(num1,"and",num2,"are not co-prime")
        break
else:
    print(num1,"and",num2,"are co-prime")

print()
print()
