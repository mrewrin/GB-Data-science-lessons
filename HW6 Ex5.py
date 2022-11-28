class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Start drawing {self.title}"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"You took the {self.title}. Starting pen drawing"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"You took the {self.title}. Starting pencil drawing"


class Marker(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"You took the {self.title}. Start drawing with a marker"


pen = Pen("a pen")
pencil = Pencil("a pencil")
handle = Marker("a marker")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
