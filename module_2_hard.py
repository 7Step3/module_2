
num_1 = int(input('Введите число из первой вставки: '))

num_2 = []
for i in range(1, num_1):
    for j in range(1, num_1):
        if num_1 % (i + j) == 0 and i < j:
            pair = str(i) + str(j)
            num_2.append(pair)
print('Число из второй вставки (решение ребуса):',''.join(num_2))