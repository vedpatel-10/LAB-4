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

