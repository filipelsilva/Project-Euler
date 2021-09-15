def decimalToBinary(n):
    return bin(n).replace("0b", "")

def palindrome(n):
    return str(n) == str(n)[::-1] and decimalToBinary(n) == decimalToBinary(n)[::-1]

soma = 0

for i in range(1000001):
    if palindrome(i):
        soma += i

print(soma)
