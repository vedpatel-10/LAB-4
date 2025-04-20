s = input("Enter a string: ")
count_alpha = 0
count_num = 0
new_str = ""

for i in s:
    if ord(i)>=65 and ord(i)<=90:
        count_alpha = count_alpha + 1 
    elif ord(i)>= 97 and ord(i)<=122:
        count_alpha = count_alpha +1                  

for j in s:
    new_str = new_str + j
    if new_str.isdigit():
        count_num = count_num + 1
    del(new_str)
    new_str = ""

print("Total alphabets in string are : "+str(count_alpha))        
print("Total digits in string are : "+ str(count_num))

#OUTPUT:
# Enter a string: I ate 4 mangoes.
# Total alphabets in string are : 11
# Total digits in string are : 1
