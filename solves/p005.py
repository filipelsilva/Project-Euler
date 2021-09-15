def accept(num):
    for i in range(1, 21):
        if num % i != 0:
            return False

    return True

i = 20

while True:
    if accept(i):
        print(i)
        break
    else:
        i += 1
