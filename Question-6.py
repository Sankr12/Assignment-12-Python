# Write a python script to print first N prime numbers

print()
num = int(input("Enter a number: "))
b=1

while num>0:
    b=b+1
    for i in range(2,b):
        if b%i==0:
            break
    else:
        print(b,end=' ')
        num-=1
print()
print()