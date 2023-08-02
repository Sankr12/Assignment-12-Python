# Write a python script to check whether a given number is prime or not

print()
num = int(input("Enter a number: "))

for i in range(2,num):
    if num%i==0:
        print(num,"is not a prime number")
        break
    else:
        pass
else:
    print(num,"is a prime number")

print()