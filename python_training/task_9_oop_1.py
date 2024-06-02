from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


class Link(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


search = Input('input#search', 'input')
print(search.check_text())

home = Button('button#home', 'button')
print(home.check_text())

h1 = Title('title#h1', 'title')
print(h1.check_text())

url = Link('link#url', 'link')
print(url.check_text())
