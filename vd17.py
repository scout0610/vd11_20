print("nhap sai so epsilon: ")
e = float(input())

sum = 0
x = 1
d = 1
i = 0
while x*d >e:
    sum = sum + x
    i = i+1
    d = -d
    # x = float(d/(2*i + 1))
    x = float(d)/float(2*i+1)
print(sum *4)
