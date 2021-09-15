for n in range(1,1001):
    for m in range(n,1001):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a + b + c == 1000:
            print(a*b*c)
            break
