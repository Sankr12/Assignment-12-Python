# Write a python script to print first N prime numbers

print()
num = int(input("Enter a number: "))
a=0
b=1

while a<num:
    b=b+1
    for i in range(2,b):
        if b%i==0:
            break
    else:
        print(b,end=' ')
        a=a+1
print()
print()