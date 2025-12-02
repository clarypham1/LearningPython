class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def info(self):
        print(f"name: {self.name}, calories: {self.calories}")

#Main programme
class Fruit(Food):
    def __init__(self, name, calories, is_sweet):
        super().__init__(name, calories)
        self.is_sweet = is_sweet

    def info(self):
        super().info()
        print(f"Sweet: {'Yes' if self.is_sweet else 'No'}")

fruit =Fruit("apple", 20, True)
fruit.info()