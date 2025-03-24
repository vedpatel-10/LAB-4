num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("Number is prime")
else:
    print("Number is not prime")

int(num)
lst = []

for i in range(1, num):
    if (num % i == 0):
        lst.append(i)

if sum(lst) == num :
    print("Number is perfect")
else:
    print("Number is not perfect")

reverse = 0
num1 = num 
while (num1!= 0):
    r = num1 % 10
    reverse = (reverse*10) + r
    num1 = num1//10 

if reverse == num:
    print("Number is palindrome")    
else:
    print("Number is not palindrome")    

num2 = num
num_len = len(str(num))
num3 =0

while num2!=0:
    r = num2 %10
    num3 = num3 + r**num_len
    num2 = num2//10
if num3 == num:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")    

num_str = str(num)
square_str = str(num**2)
if (num_str in square_str) :
    print("Number is automorphic")
else:
    print("Number is not automorphic")    
