# Write a python script to print first N terms of a Fibonacci series

print()
num = int(input("Enter a number: "))
a=0
b=1

while num:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    num-=1
    
print()