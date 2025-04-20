limit = int(input("Enter a number for maximum limit: "))
i =0 
j = 1

print(i)
print(j)
res = i +j

while res<=limit:
    print(res)
    i = j 
    j = res 
    res = i + j

#OUTPUT:
# Enter a number for maximum limit: 6
# 0
# 1
# 1
# 2
# 3
# 5
