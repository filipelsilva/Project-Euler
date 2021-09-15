def recurringLen(num):
    remainders = []
    tmp = 0
    uno = 1

    while True:
        tmp = uno % num
        uno *= 10

        if tmp not in remainders:
            remainders += [tmp] 
        else:
            return len(remainders) - remainders.index(tmp)

lenght = 0
num = 0

for i in range(1,1001):
    tmp = recurringLen(i)
    
    if tmp > lenght:
        lenght = tmp
        num = i

print(num)
