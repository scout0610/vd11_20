
n = int(input())
print("so fibonaci nho hon n: ")
f1 = 1
f2 = 1
list_fibo = [f1, f2]
while f1 + f2 < n:
    f = f1+f2
    list_fibo.append(f)
    f1 = f2
    f2 = f

print(list_fibo)


