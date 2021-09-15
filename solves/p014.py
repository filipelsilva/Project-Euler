def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def countCollatz(num):
    count = 1
    while num != 1:
        num = collatz(num)
        count += 1
    return count

maxcount = 0
maxnum = 0

for i in range(100,1000001):
    tmp = countCollatz(i)
    if tmp > maxcount:
        maxcount = tmp
        maxnum = i

print(maxnum)
