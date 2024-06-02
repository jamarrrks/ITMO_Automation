class Car:

    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year

    def one(self):
        print('Автомобиль заведен')

    def two(self):
        print('Автомобиль заглушен')

    def three(self, year):
        self.year = year
        return self.year

    def four(self, type):
        self.type = type
        return self.type

    def five(self, color):
        self.color = color
        return self.color


bmw = Car()
bmw.one()
bmw.two()
print('Год выпуска:', bmw.three('2020'))
print('Тип:', bmw.four('M3'))
print('Цвет:', bmw.five('Yellow'))






