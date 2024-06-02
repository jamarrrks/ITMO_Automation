class Soda:

    def __init__(self, dop=None):
        self.dop = dop

    def show_my_drink(self):
        if self.dop:
            print(f'Газировка и {self.dop}')
        else:
            print('Обычная газировка')


drink1 = Soda()
drink1.show_my_drink()
drink2 = Soda('Lime')
drink2.show_my_drink()
