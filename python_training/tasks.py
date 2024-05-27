def function1(a=(1, 2, 3, 4)):
    return a[1]

print(function1())


def function2(radius, pi=3.14159):
    return pi * (radius ** 2)

print(function2(3))


def function3(string: str = '') -> int:
    return len(string)

print(function3())


def function4(one: list, two: list) -> int:
    return max(len(one), len(two))

print(function4([1, 2, 3], [1, 2]))


def function5(random_list: list) -> list:
    random_list.append('hello')
    return random_list

print(function5([1, 2]))


def function6(number_list: list) -> int:
    sum = 0
    for elem in number_list:
        sum = sum + elem
    return sum

print(function6([1, 2, 3, 4]))