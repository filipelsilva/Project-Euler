def factorial(num):
    ret = 1
    for i in range(1,num+1):
        ret *= i
    return ret

num = factorial(100)

soma = 0

for el in str(num):
    soma += int(el)

print(soma)
