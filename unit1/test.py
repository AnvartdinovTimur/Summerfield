print('Введите целые числа, каждое в отдельной строке.')
print('Или просто нажмите Enter для выхода')

total = 0
count = 0

while True:
    line = input('Число: ')
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break

if count:
    print('Введено чисел: {0}, сумма: {1}, среднее: {2}'\
        .format(count, total, total / count))
