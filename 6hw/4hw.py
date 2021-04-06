class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f"current speed is {self.speed}"

    def go(self):
        return f"{self.name} (Going)\n"

    def stop(self):
        return f"{self.name} (Stopped)\n"

    def turn(self, direction):
        if direction == "left":
            return f"{self.name} (turning left)\n"
        if direction == "right":
            return f"{self.name} (turning right)\n"
        else:
            ValueError("Wrong value")


class TownCar(Car):
    Car.name = "TownCar"

    def show_speed(self):
        if self.speed < 60:
            return f"current speed is {self.speed}\n"
        else:
            return f"whoa,man your speed is {self.speed} , slow down\n"


class SportCar(Car):
    Car.name = "SportCar"

    def show_speed(self):
        if self.speed > 60:
            return f"current speed is {self.speed}\n"
        else:
            return f"speed is {self.speed} . Push datt button under your right feet\n"


class WorkCar(Car):
    Car.name = "WorkCar"

    def show_speed(self):
        if self.speed < 40:
            return f"current speed is {self.speed},don`t forget your bucket of coffee\n"
        else:
            return f"speed is {self.speed} . have a mercy you have wife and kids\n"


class PoliceCar(Car):
    Car.name = "PoliceCar"

    def show_speed(self):
        return "Woop - woop! That's the sound of da police\nWoop - woop! That's the sound of da beast"


car = TownCar(100, "blue", "R u nuts? cars dont have a name", True)
print(car.go())
print(car.show_speed())
print(car.turn("left"))
print(car.turn("right"))
print(car.stop())
