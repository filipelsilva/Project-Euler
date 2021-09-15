def nameHash(name):
    ret = 0
    for el in name.replace('"', ''):
        ret += ord(el) - 64
    return ret

with open('../inputs/p022_names.txt', 'r') as file:
    names = sorted(file.read().replace('"', '').split(','))

soma = 0

for i in range(len(names)):
    soma += (i+1) * nameHash(names[i])

print(soma)

