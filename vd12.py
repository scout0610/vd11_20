import math

n = int(input("nhap n: "))
h = set(range(3,n))
print("cac so nguyen to nho hon " + str(n))
a = [i for i in range(2,n) for j in range(2, math.ceil(math.sqrt(i))+1 ) if i%j == 0]
b = list(h.symmetric_difference(a))
print(b)


