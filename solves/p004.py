def isPalindrome(num):
    number = str(num)
    return number == number[::-1]

pal = 0

for i in range(999,0,-1):
    for j in range(999,0,-1):
        num = i * j
        if isPalindrome(num) and num > pal:
            pal = num

print(pal)
