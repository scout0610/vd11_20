n = int(input("nhap n: "))
x = '*'
s = ' '

# tam giác vuông trái
print("tam giác vuông trái")
l = [print(x*i) for i in range(1,n+1)]

# tam giác vuông phải
print("tam giác vuông phải")
r = [print(s*(n-i) + x*i) for i in range(1,n+1)]

#tam giác cân
print("tam giác cân")
c = [print(s*(n-i) + x*(2*i-1)) for i in range(1,n+1)]
