class Dog():

    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name+" say woof!"


class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name+" say meow!"

niko = Dog("niko")
felix = Cat("felix")

print(felix.speak())
print(niko.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak))

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)


class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")