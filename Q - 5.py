def find_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(1, limit + 1): 
            c = (a**2 + b**2) ** 0.5  
            if c.is_integer() and c <= limit:
                triplets.append([a, b, int(c)])

    return triplets

limit = 30
triplets = find_pythagorean_triplets(limit)
for i in triplets:
    print(i)

#OUTPUT:
# [3, 4, 5]
# [4, 3, 5]
# [5, 12, 13]
# [6, 8, 10]
# [7, 24, 25]
# [8, 6, 10]
# [8, 15, 17]
# [9, 12, 15]
# [10, 24, 26]
# [12, 5, 13]
# [12, 9, 15]
# [12, 16, 20]
# [15, 8, 17]
# [15, 20, 25]
# [16, 12, 20]
# [18, 24, 30]
# [20, 15, 25]
# [20, 21, 29]
# [21, 20, 29]
# [24, 7, 25]
# [24, 10, 26]
# [24, 18, 30]  
