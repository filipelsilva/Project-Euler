def factorial(num):
    ret = 1
    for i in range(1,num+1):
        ret *= i
    return ret

def combinations(n, k):
    ret = factorial(n)
    ret /= (factorial(n-k)*factorial(k))
    return ret

k = 20
n = 20

print(combinations(k+n, k))
