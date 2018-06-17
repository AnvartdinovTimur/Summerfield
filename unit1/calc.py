count = 0
summa = 0
minimum = 99999999
maximum = -99999999
numbers =[]

while True:
    try:
        line = input('Введите число или нажмите Enter для выхода: ')
        if line is '':
            break
        number = int(line)
        numbers += [number]
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
        summa += number
        count += 1
    except ValueError as err:
        print(err)

print(numbers)
print('Количество = {0}, сумма = {1}, минимум = {2}, максимум = {3},\
        среднее = {4}'.format(count, summa, minimum, maximum, summa / count))
