def fraction(n1, n2):
    if n1 == n2:
        return 1, 1

    t1 = str(n1)
    t2 = str(n2)
    num = ""
    den = ""

    if t1[0] == t2[0]:
        return int(t1[1]), int(t2[1])

    if t1[1] == t2[1]:
        return int(t1[0]), int(t2[0])

    for el in t1:
        if el not in t2 or int(el) == 0:
            num += el

    for el in t2:
        if el not in t1 or int(el) == 0:
            den += el

    if num == "" and den == "":
        return 1, 1

    return int(num), int(den)

def check(numerator, denominator, num, den):
    if numerator >= denominator:
        return False
    elif numerator == num:
        return False
    elif den == 0 or num == 0:
        return False
    elif numerator/num == 10 and denominator/den == 10:
        return False
    elif float(numerator)/float(denominator) == float(num)/float(den):
        print(str((numerator, denominator)) + " -> " + str((num, den)) + " TRUE")
        return True
    else:
        # print(str((numerator, denominator)) + " -> " + str((num, den)) + " FALSE")
        return False

fractions = []

for numerator in range(10,100):
    for denominator in range(10,100):
        num, den = fraction(numerator, denominator)
        if check(numerator, denominator, num, den):
            fractions += [(num,den)]

print(fractions)

num = 1
den = 1

for el in fractions:
    num *= el[0]
    den *= el[1]

print(num, den)
