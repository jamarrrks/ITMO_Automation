def function1():
    str_1 = 'test'
    str_2 = 'test1'

    if str_1 in str_2:
        return 'Yes'
    else:
        return 'No'


print(function1())


def function2(year: int):
    if year == 1 or year == 2 or year == 3 or year == 4:
        return 'Бакалавр'
    elif 5 <= year <= 6:
        return 'Магистр'
    elif 7 <= year <= 9:
        return 'Аспирант'


print(function2(6))


def function3(num: int):
    if num < -100 or num > 100:
        print('-')
    else:
        print('+')


function3(54)