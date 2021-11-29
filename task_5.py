class Stationery:

    def __init__(self, title):
        self.title = title
    def draw(self):
        return 'Drowing begins!'

crayon = Stationery('crayon').draw()
print(crayon)

class Pen(Stationery):

    def draw(self):
        return 'Drawing begins by blue color!'
pen = Pen('pen').draw()
print(pen)

class Pencil(Stationery):
    def draw(self):
        return 'You can make draft of your pictures!'
pencil = Pencil('pecil').draw()
print(pencil)

class Handle(Stationery):
    def draw(self):
        return 'You draw bold'

handle = Handle('handle').draw()
print(handle)
