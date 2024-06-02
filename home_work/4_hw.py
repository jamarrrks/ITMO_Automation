class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        print('Периметр =', (self.width + self.height) * 2)

    def area(self):
        print('Площадь =', self.width * self.height)


rec1 = Rectangle(2, 4)
print('Треугольник 1:')
rec1.perimeter()
rec1.area()
print('\n')

rec2 = Rectangle(8, 3)
print('Треугольник 2:')
rec2.perimeter()
rec2.area()
print('\n')

rec3 = Rectangle(2, 5)
print('Треугольник 3:')
rec3.perimeter()
rec3.area()
print('\n')


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f'Сумма = {self.a + self.b}')

    def multiplication(self):
        print(f'Произведение = {self.a * self.b}')

    def division(self):
        print(f'Частное = {self.a / self.b}')

    def substraction(self):
        print(f'Разность = {self.a - self.b}')


numbers = Math(2, 1)
numbers.addition()
numbers.multiplication()
numbers.division()
numbers.substraction()


class Sidebar:

    def __init__(self, text, type='Buttons', loc=''):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text}')


text_box = Sidebar('Text Box')
print(text_box.text)
text_box.click()

check_box = Sidebar('Check Box')
print(check_box.text)
check_box.click()

radio_button = Sidebar('Radio Button')
print(radio_button.text)
radio_button.click()

web_tables = Sidebar('Web Tables')
print(web_tables.text)
web_tables.click()

buttons = Sidebar('Buttons')
print(buttons.text)
buttons.click()

links = Sidebar('Links')
print(links.text)
links.click()

