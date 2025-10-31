class Car:
    def _init_(self, brand, color, mileage = 0, fuel = 100):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, distance):
        fuel_needed = distance * 0.5
        if self.fuel >= fuel_needed:
            self.mileage += distance
            self.fuel -= fuel_needed
            print(f"The car drove {distance} km. Remaining fuel: {self.fuel:.2f}%.")
        else:
            max_distance = self.fuel / 0.5
            self.fuel = 0
            print(f"The car ran out of fuel after driving {max_distance:.2f} km.")

        print(f"Driven {distance} km. Total mileage is now {self.mileage} km.")
        print(f"The car your driving is a {self.brand} in the color {self.color}")

    def repaint(self, color2):
        self.color = color2
        print(f"The {self.brand} was repainted with the color {self.color}")

car1 = Car("BMW", "red")
car2 = Car("Mercedes", "blue")

car1.drive(10)
car2.drive(60)

car1.drive(100)
car1.repaint("blue")

car2.drive(200)
car2.repaint("red")