# Write a python script to print all prime numbers under 100

print()

for i in range(2,100):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        print(i,end=' ')

print()
print()