class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Drawing Starts"


class Pen(Stationary):
    def draw(self):
        return "Pen Drawing Starts"


class Pencil(Stationary):
    def draw(self):
        return "Pencil Drawing Starts"


class Handle(Stationary):
    def draw(self):
        return "Handle Drawing Starts"


s = Stationary("jist a bunch of text")
p = Pen("jist a bunch of some text")
P=Pencil("jist a bunch of any text")
h=Handle("jist a text")
print(s.draw())
print(p.draw())
print(P.draw())
print(h.draw())
