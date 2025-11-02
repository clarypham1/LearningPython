class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def main():
    car = Car("ABC-123", 142)
    print("Initial car information:")
    print(f"Registration number: {car.registration_number}")
    print(f"Maximum speed: {car.maximum_speed} km/h")
    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance} km")
    print()
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(f"Current speed after accelerations: {car.current_speed} km/h")
    car.accelerate(-200)
    print(f"Final speed after emergency brake: {car.current_speed} km/h")
    print()
    car.current_speed = 60
    car.travelled_distance = 2000
    car.drive(1.5)
    print(f"Travelled distance after driving: {car.travelled_distance} km")

if __name__ == "__main__":
    main()

#4)
import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_number = f"ABC-{i}"
        cars.append(Car(reg_number, max_speed))

    race_finished = False
    hours_passed = 0

    while not race_finished:
        hours_passed += 1
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_finished = True
                break

    print(f"\n Race finished in {hours_passed} hours!\n")
    print(f"{'Car':<10}{'Max Speed (km/h)':<20}{'Current Speed (km/h)':<22}{'Distance (km)':<15}")
    print("-" * 67)
    for car in cars:
        print(f"{car.registration_number:<10}{car.maximum_speed:<20}{car.current_speed:<22}{car.travelled_distance:<15.1f}")


if __name__ == "__main__":
    main()


