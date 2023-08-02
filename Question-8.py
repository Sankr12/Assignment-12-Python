# Write a python script to print first N terms of a Fibonacci series

print()
num = int(input("Enter a number: "))
a=0
b=1
c=0
count = 0

while count<num:
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    count+=1
    
print()