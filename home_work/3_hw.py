def task_1(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)


task_1(7.5, 7)


def task_2(num1, num2):
    if num1 - num2 == 135 or num2 - num1 == 135:
        print('Yes')
    else:
        print('No')


task_2(136, 1)


def task_3(month: int):
    if month == 12 or month in range(1, 3):
        print('Зима')
    elif month in range(3, 6):
        print('Весна')
    elif month in range(6, 9):
        print('Лето')
    elif month in range(9, 12):
        print('Осень')
    else:
        print('Введите число от 1 до 12')


task_3(12)


def task_4(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print('Yes')
    else:
        print('No')


task_4(10.1, 9.9, 13)


def task_5(numbers: list):
    count = 0
    for elem in numbers:
        if elem > 0:
            count = count + 1
    return count


print(task_5([-3, 0, 3, 3, 5]))


def task_6(years, months: int):
    days = (months * 29) + (years * 12 * 29)
    return days


print(task_6(2, 10))
