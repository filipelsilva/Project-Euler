sumSquares = 0
squareSum = 0

for i in range(1,101):
    sumSquares += i**2
    squareSum += i

squareSum = squareSum**2

print(sumSquares - squareSum)
