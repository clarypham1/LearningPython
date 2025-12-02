class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"  Author: {self.author}")
        print(f"  Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"  Chief Editor: {self.chief_editor}")



class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def set_speed(self, speed):

        self.current_speed = min(speed, self.max_speed)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery_capacity):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, tank_volume):
        super().__init__(reg_num, max_speed)
        self.tank_volume = tank_volume


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
print()
compartment6.print_information()

print("\n--- Car Simulation ---\n")

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

electric.set_speed(140)
gasoline.set_speed(120)

electric.drive(3)
gasoline.drive(3)

# Print distances
print(f"Electric car ({electric.registration_number}) distance: {electric.travelled_distance} km")
print(f"Gasoline car ({gasoline.registration_number}) distance: {gasoline.travelled_distance} km")
