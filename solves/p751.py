from decimal import Decimal
# NOT WORKING YET
def b(prev):
    ret = int(prev)
    ret *= (prev - int(prev) + 1)
    return ret
    
def check(num):
    tmp = b(num)
    working = str(int(tmp)) + "."
    count = 0

    while len(working) != 26:
        tmp = b(tmp)
        working += str(int(tmp))

        #print(num, working)
        if working != str(num)[:len(working)]:
            return count

        count += 1

    return -2

def getBestForLevel(num, exp):
    explore = []
    checks = []
    for i in range(10):
        checks += [check(num)]
        num += Decimal(1) / (Decimal(10) ** Decimal(exp))

    best = max(checks)
    for i in range(10):
        if checks[i] == -2:
            print(str(num + Decimal(i) / (Decimal(10) ** Decimal(exp))))
        if checks[i] == best:
            explore += [num + Decimal(i) / (Decimal(10) ** Decimal(exp))]

    return explore

explore = [Decimal('2.0')]

# num = explore[0]
# exp = 1
# print(num + Decimal(2) / Decimal(10) ** Decimal(exp))

while True:
    print(explore[0])
    explore += getBestForLevel(explore[0], len(str(explore[0]))-2)
    explore.pop(0)
