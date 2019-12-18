from ast import literal_eval

with open("data.csv") as file:
    data = file.read().splitlines()

numbers = []
for x in range (len(data)):
    numbers.append(list(literal_eval(data[x])))

n = numbers[0][0]
k = numbers[0][1]

for x in range(1, len(numbers)):
    for y in range(len(numbers[x])):
        if isinstance(numbers[x][y], str):
            splitted = numbers[x][y].split('/')
            num1 = int(splitted[0])
            num2 = int(splitted[1])
            numbers[x][y] = num1/num2

numbers_new = []


numbers_new_temp = []
for y in range(n):
    temp = []
    s = 0
    for x in range(1, 1+n):
        s += numbers[x][y]
    for x in range(1, 1+n):
        temp.append(numbers[x][y]/s)
    numbers_new_temp.append(temp)
numbers_new.append(numbers_new_temp)

for z in range(1, n+1):
    numbers_new_temp = []
    for y in range(k):
        temp = []
        s = 0
        for x in range(1 + k * z, 1 + k + k * z):
            s += numbers[x][y]
        for x in range(1 + k * z, 1 + k + k * z):
            temp.append(numbers[x][y] / s)
        numbers_new_temp.append(temp)
    numbers_new.append(numbers_new_temp)

doles = []

doles_temp = []
for y in range(n):
    s = 0
    for x in range(n):
        s += numbers_new[0][x][y]
    s /= len(numbers_new[0][x])
    doles_temp.append(s)
doles.append(doles_temp)

for z in range(1, n+1):
    doles_temp = []
    for y in range(k):
        s = 0
        for x in range(k):
            s += numbers_new[z][x][y]
        s /= len(numbers_new[z][x])
        doles_temp.append(s)
    doles.append(doles_temp)
print(doles)

f = []

for i in range (n):
    f_temp = 0
    for y in range (k):
        f_temp += doles[0][y] * doles[y+1][i]
    f.append(f_temp)

print(f)