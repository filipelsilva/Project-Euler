def check(num):
    soma = 0
    for el in str(num):
        soma += int(el)**5
    return soma == num

soma = 0
for i in range(10,1000000):
    if check(i):
        print(i)
        soma += i

print(soma)
