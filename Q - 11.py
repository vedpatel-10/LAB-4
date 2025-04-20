import math
degrees = int(input("Enter the degree: "))
rad = (degrees * 3.14)/180
result = 0

for i in range(0,4):
    coefficient = (-1)**i
    numerator = rad**(2*i +1)
    denominator = math.factorial(2*i + 1)
    result = result + (coefficient*numerator)/denominator 

print(result)    

#OUTPUT:
# Enter the degree: 45
# 0.7068248709111208
