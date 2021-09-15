def moveUp(x, y):
    return x, y - 1

def moveDown(x, y):
    return x, y + 1

def moveLeft(x, y):
    return x - 1, y

def moveRight(x, y):
    return x + 1, y

spiral = [[0 for x in range(1001)] for y in range(1001)]

spiral[500][500] = 1
x = 500
y = 500
count = 2

for i in range(1,1001):
    if i % 2 == 0:
        for j in range(i):
            x, y = moveLeft(x, y)
            spiral[y][x] = count
            count += 1

        for j in range(i):
            x, y = moveUp(x, y)
            spiral[y][x] = count
            count += 1
    else:
        for j in range(i):
            x, y = moveRight(x, y)
            spiral[y][x] = count
            count += 1

        for j in range(i):
            x, y = moveDown(x, y)
            spiral[y][x] = count
            count += 1

for j in range(1001-1):
    x, y = moveRight(x, y)
    spiral[y][x] = count
    count += 1

soma = 0

for x in range(1001):
    soma += spiral[x][x]
    soma += spiral[x][1000-x]

print(soma - 1)
