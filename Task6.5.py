class Stationery:

    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f'Just start drawing! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Just start drawing with Pen! {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Just start drawing with Pencil! {self.title}')


class Marker(Stationery):
    def draw(self):
        print(f'Just start drawing with Marker! {self.title}')