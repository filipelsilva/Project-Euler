with open('../inputs/p067_triangle.txt', 'r') as file:
    lines = file.readlines()

triangle = []

for i in range(len(lines)):
    triangle += [lines[i].replace('\n', '').split(' ')]
    for j in range(len(triangle[i])):
        triangle[i][j] = int(triangle[i][j])

#print(triangle)

for i in range(len(triangle)-1,-1,-1):
    for j in range(len(triangle[i])-1):
        triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])

print(triangle[0][0])
