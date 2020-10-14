
a = int(input())
b = int(input())

min = min(a,b)
max = max(a,b)
# ucln
print("ucln: ")
list_min = list(range(1,min+1))
list_uc = [i for i in list_min[::-1] if max%i == 0 and min % i ==0]
print(list_uc[0])

#bscnn
print("bscnn: ")
list_max = list(range(max, a*b+1))
list_bc = [i for i in list_max if i%max ==0 and i%min ==0]
print(list_bc[0])