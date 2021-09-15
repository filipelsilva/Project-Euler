def factorial(num):
    ret = 1
    for i in range(1,num+1):
        ret *= i
    return ret

def check(num):
    soma = 0
    for el in str(num):
        soma += factorial(int(el))
    return soma == num

soma = 0
for i in range(3,1000000):
    if check(i):
        soma += i
        print(i)

print(soma)
