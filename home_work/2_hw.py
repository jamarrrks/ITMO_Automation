def task_1() -> tuple:
    a: int = 1
    b: float = 2.35
    c: str = 'hello world'
    d: list = ['one', 'two', 3]
    e: bool = True
    return type(a), type(b), type(c), type(d), type(e)


print(task_1())


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


print(task_2())


def task_3(number: int) -> int:
    return number ** 2


print(task_3(32))