# Write a python script to print all prime numbers between two given numbers(both number inclusive)

print()
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1<=1:
    num1=2
for i in range(num1,num2+1):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        print(i,end=' ')

print()
print()