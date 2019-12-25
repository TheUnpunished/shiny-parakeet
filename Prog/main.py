from ast import literal_eval

with open("data.csv") as file:
    data = file.read().splitlines()

numbers = []
for x in range (len(data)):
    numbers.append(list(literal_eval(data[x])))

n = numbers[0][0]
k = numbers[0][1]

names = numbers[1]
criteria_names = numbers[2]

for x in range(3, len(numbers)):
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
    for x in range(3, 3+n):
        s += numbers[x][y]
    for x in range(3, 3+n):
        temp.append(numbers[x][y]/s)
    numbers_new_temp.append(temp)
numbers_new.append(numbers_new_temp)

for z in range(1, n+1):
    numbers_new_temp = []
    for y in range(k):
        temp = []
        s = 0
        for x in range(3 + k * z, 3 + k + k * z):
            s += numbers[x][y]
        for x in range(3 + k * z, 3 + k + k * z):
            temp.append(numbers[x][y] / s)
        numbers_new_temp.append(temp)
    numbers_new.append(numbers_new_temp)


deriv = []

deriv_temp = []
for y in range(n):
    s = 0
    for x in range(n):
        s += numbers_new[0][x][y]
    s /= len(numbers_new[0][x])
    deriv_temp.append(s)
deriv.append(deriv_temp)

print("Нормированные таблицы и средние значения:")
print("Критерии: ")

for x in range(n):
    out_str = ""
    for y in range(n):
        out_str += str(numbers_new[0][y][x]) + " "
    out_str += str(deriv[0][x])
    print(out_str)

for z in range(1, n+1):
    deriv_temp = []
    for y in range(k):
        s = 0
        for x in range(k):
            s += numbers_new[z][x][y]
        s /= len(numbers_new[z][x])
        deriv_temp.append(s)
    deriv.append(deriv_temp)

for z in range(1, n+1):
    print(criteria_names[z-1])
    for x in range(k):
        out_str = ""
        for y in range(k):
            out_str += str(numbers_new[z][y][x]) + " "
        out_str += str(deriv[z][x])
        print(out_str)
f = []

for i in range (n):
    f_temp = 0
    for y in range (k):
        f_temp += deriv[0][y] * deriv[y + 1][i]
    f.append(f_temp)

print("Подсчёт альтернатив: ")

for i in range(len(f)):
    print(names[i] + " :" + str(f[i]))

print("Лучшая альтернатива: " + names[f.index(max(f))])
