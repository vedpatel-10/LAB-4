n = int(input("Enter n: "))
r = int(input("Enter r: "))
n_fact = 1
r_fact = 1
n_r = n-r
n_r_fact = 1

for i in range(1,n+1):
    n_fact = n_fact*i

for j in range(1,r+1):
    r_fact = r_fact * j

for k in range(1,(n_r)+1):
    n_r_fact = n_r_fact * k

print("NPR :")
print(n_fact/n_r_fact)    

print("NCR :")
print(n_fact / (n_r_fact * r_fact))

#OUTPUT:
# Enter n: 5
# Enter r: 3
# NPR :
# 60.0
# NCR :
# 10.0
