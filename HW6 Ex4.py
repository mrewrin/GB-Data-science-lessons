class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f"{self.name} is started"

    def stop(self):
        return f"{self.name} is stopped"

    def turn_right(self):
        return f"{self.name} is turned right"

    def turn_left(self):
        return f"{self.name} is turned left"

    def show_speed(self):
        return f"Current speed {self.name} is {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed of town car {self.name} is {self.speed}")

        if self.speed > 40:
            return f"Speed of {self.name} is higher than allow for town car"
        else:
            return f"Speed of {self.name} is normal for town car"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current speed of work car {self.name} is {self.speed}")

        if self.speed > 60:
            return f"Speed of {self.name} is higher than allow for work car"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} is from police department"
        else:
            return f"{self.name} is not from police department"


ferrari = SportCar(250, "Red", "Ferrari", False)
smart = TownCar(30, "White", "Smart", False)
toyota = WorkCar(70, "Black", "Toyota", True)
bugatti = PoliceCar(110, "NYPD color",  "Bugatti", True)
print(toyota.turn_left())
print(f"When {smart.turn_right()}, then {ferrari.stop()}")
print(f"{toyota.go()} with speed exactly {toyota.show_speed()}")
print(f"{toyota.name} is {toyota.color}")
print(f"Is {ferrari.name} a police car? {ferrari.is_police}")
print(f"Is {toyota.name} a police car? {toyota.is_police}")
print(ferrari.show_speed())
print(smart.show_speed())
print(bugatti.police())
print(bugatti.show_speed())
