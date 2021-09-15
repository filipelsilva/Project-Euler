n1 = 1
n2 = 0
count = 1
num = 1

while len(str(num)) < 1001:
    count += 1
    num = n1 + n2
    n2 = n1
    n1 = num
    print(num, len(str(num)), count)
