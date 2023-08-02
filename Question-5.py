# Write a python script to find next prime number of a given number

print()
num = int(input("Enter a number: "))
b=num
if num<1:
    num=1

while num>0:
    num=num+1
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print()
        print("Next prime number of",b,"is",num)
        break
print()
print()