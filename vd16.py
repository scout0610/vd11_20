n = int(input())
a = []
a.append(n)
while n!=0:
    n = int(input())
    a.append(n)

sum_even = [i for i in a if i % 2==0]
sum_odd = [i for i in a if i % 2==1]
print("Tong cac so chan la: " + str(sum(sum_even)))
print("Tong cac so le la: " + str(sum(sum_odd)))