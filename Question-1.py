# Write a python  script to reverse a number

print()
num = int(input("Enter a number: "))
i = num
string=''

while num>0:
    a=num%10
    string=string+str(a)
    num//=10

print("Reverse of",i,"=",string)
print()