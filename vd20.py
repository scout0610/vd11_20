print("phan tu mang: ")
n = int(input())
print("nhap phan tu mang: ")
a = [int(input()) for _ in range(n)]

a = [i for i in a if i%2 !=0]
print("mang sau khi xoa so chan")
print(a)