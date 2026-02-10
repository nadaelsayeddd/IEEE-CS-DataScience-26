import math
n = input()

lst = []

for i in n:
    lst.append(int(i))

summation = 0

for i in lst:
    summation += pow(i,len(n))

if int(n) == summation:
    print(f"{n} is an Armstrong number")
else:
    print("Please, Enter an Armstrong number")

