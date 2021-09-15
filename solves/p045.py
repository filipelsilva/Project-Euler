def triangle(n):
    return n * (n + 1) / 2

def pentagonal(n):
    return n * (3 * n - 1) / 2

def hexagonal(n):
    return n * (2 * n - 1)

tria = {triangle(i) for i in range(1,1000001)}
pent = {pentagonal(i) for i in range(1,1000001)}
hexa = {hexagonal(i) for i in range(1,1000001)}

for el in tria:
    if el in pent and el in hexa:
        print(el)
