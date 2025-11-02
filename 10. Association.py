class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}.")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}.")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print("Error: Target floor is out of range.")
            return

        print(f"Moving from floor {self.current_floor} to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}.\n")


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))
        print(f"Building created with {number_of_elevators} elevators "
              f"from floor {bottom_floor} to {top_floor}.\n")

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Error: Invalid elevator number.")
            return

        print(f"Running elevator {elevator_number} to floor {destination_floor}:")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("🚨 Fire alarm activated! Moving all elevators to the bottom floor...\n")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Elevator {i}:")
            elevator.go_to_floor(elevator.bottom_floor)
        print("All elevators are now at the bottom floor.\n")


def main():
    building = Building(1, 10, 3)
    building.run_elevator(1, 5)
    building.run_elevator(2, 8)
    building.fire_alarm()


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
        # Keep speed within valid limits
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n🏁 {self.name} — Race status")
        print(f"{'Car':<10}{'Max Speed (km/h)':<20}{'Current Speed (km/h)':<22}{'Distance (km)':<15}")
        print("-" * 67)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.maximum_speed:<20}{car.current_speed:<22}{car.travelled_distance:<15.1f}")
        print()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


def main():
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        reg_number = f"ABC-{i}"
        cars.append(Car(reg_number, max_speed))
    race = Race("Grand Demolition Derby", 8000, cars)
    hours_passed = 0

    print(f"Starting the {race.name} ({race.distance} km)!\n")

    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1
        if hours_passed % 10 == 0:
            print(f"⏱ Hour {hours_passed}")
            race.print_status()
    print(f"Race finished in {hours_passed} hours!")
    race.print_status()


if __name__ == "__main__":
    main()
