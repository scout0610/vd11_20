import math
print("nhap so phan tu n: ")
n = int(input())
print("nhap phan tu mang: ")
a = [[i, abs(int(input()))] for i in range(n) ]
b = sorted([number for i,number in a] )
b.reverse()

index = [i for i,j in a if j == b[0]]
print(index)