#class Dog:
    #pass
#dog = Dog()
#dog.name = "Bubbles"
#dog.birth_year = 2002
#print(f"{dog.name:s} was born in {dog.birth_year:d}.")

#class Dog:
    #def __init__(self, name, birth_year):
        #self.name = name
        #self.birth_year = birth_year
#dog1 = Dog("Bubbles", 2002)
#dog2 = Dog("EBje", 2007)

#print(f"{dog1.name:s} was born in {dog2.birth_year:d}.")


class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    def __init__(self):
        self.dogs= []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name +  " checked in")
        return
    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name +  " checked out")
        return
    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(2)

dog1 = Dog("dhdjj",  1999)
dog2 = Dog("hhh",  2343, "yip")
hotel = Hotel()
hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()

