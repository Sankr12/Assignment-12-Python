# Write a python  script to reverse a number

print()
num = int(input("Enter a number: "))
i = num
a=0

while num>0:
    b=num%10
    a=b+a*10
    num=num//10

print("Reverse of",i,"=",a)
print()
