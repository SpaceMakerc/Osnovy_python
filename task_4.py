class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The car {self.name} is driving'
    def stop(self):
        return f'The car {self.name} has stopped'
    def direction(self, direction):
        return f'The car {self.name} has turned {direction}'
    def show_speed(self):
            return f'Speed of car {self.name}, is - {self.speed} km\ч'
subaru = Car(70, 'blue', 'Subaru', False)
a = 'Left'
print(f'{subaru.go()}\n{subaru.direction(a)}\n{subaru.stop()}\n{subaru.show_speed()}')

class TownCar(Car):
        def show_speed (self):
            if self.speed > 60:
                return 'You have exceeded the speed limit - 60 km\ч'
            else:
                return 'Nice speed!'
ford = TownCar(40, 'red', 'Ford', False)
toyota = TownCar(65, 'white', 'Toyota', False)
mercedes = TownCar(80, 'black', 'Mercedes', False)
print(f'Ford -{TownCar.show_speed(ford)}\nMersedes -{TownCar.show_speed(mercedes)}\nToyota -{TownCar.show_speed(toyota)}')

class SportCar(Car):
    def full_inform (self):
        return self.speed, self.color, self.name, self.is_police
ferrari = SportCar(100, 'yellow', 'Ferrari', False)
lamborghini = SportCar(110, 'red', 'Lamborghini', False)
porsche = SportCar(100, 'gold', 'Porsche', False)
print(f'Ferrari -{SportCar.full_inform(ferrari)}\nLamborghini -{SportCar.full_inform(lamborghini)}\nPorsche -{SportCar.full_inform(porsche)}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'You have exceeded the speed limit - 40 km\ч'
        else:
            return 'Nice speed!'
renault = WorkCar(40, 'gray', 'Renault', False)
hyundai = WorkCar(50, 'blue', 'Hyundai', False)
mazda = WorkCar(60, 'red', 'Mazda', False)
print(f'Renault -{WorkCar.show_speed(renault)}\nHyundai -{WorkCar.show_speed(hyundai)}\nMazda -{WorkCar.show_speed(mazda)}')

class Police_Car(Car):
    def full_inform(self):
        return self.speed, self.color, self.name, self.is_police
brabus = Police_Car(60, 'gray', 'Brabus', True)
audi = Police_Car(70, 'blue', 'Audi', True)
qia = Police_Car(60, 'red', 'Qia', True)
print(f'Brabus -{Police_Car.full_inform(brabus)}\nAudi -{Police_Car.full_inform(audi)}\nQia -{Police_Car.full_inform(qia)}')
