class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def computing_mass (self, mass, number_thick):
        result = self._length * self._width * mass * number_thick
        return result

road_1 = Road(2, 2)
counter = road_1.computing_mass(2, 2)
print(f'Computing mass is {counter} т')
