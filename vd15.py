import math
n = int(input())
list_uoc = [i for i in range(1, math.ceil(n/2) +1) if n%i == 0]
sum_uoc = sum(list_uoc)

if n == sum_uoc:
    print("n là số hoàn hảo")
else:
    print("n không là số hoàn hảo")