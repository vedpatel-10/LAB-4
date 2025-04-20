num = int(input("Enter a number: "))
count = 0
for i in range(1,num+1):
    if (num%i==0):
        count =count+1 

if count ==2:
    print("Prime number!")
else:
    print("Number is not prime!")

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
new_str = square_str[-1 *(len(num_str)) :]

if (num_str == new_str) :
    print("Number is automorphic")
else:
    print("Number is not automorphic")  

#OUTPUT:
# Enter a number: 5
# Prime number!
# Number is not perfect
# Number is palindrome
# Number is Armstrong
# Number is automorphic
