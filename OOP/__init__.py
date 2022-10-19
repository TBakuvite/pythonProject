class Dog():

    species = 'mammal'


    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self,number):
        print(f'WOOF! My name is {self.name} and my number is {number}')


my_dog = Dog(breed='lab',name='Roberto',spots=False)

print(type(my_dog))
print(my_dog.breed)
print(my_dog.spots)
print(my_dog.name)

my_dog = Dog('Lab','Sam',False)
print(type(my_dog))
print(my_dog.name)
print(my_dog.species)
my_dog.bark(10)


class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius*self.pi*2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.get_circumference())





