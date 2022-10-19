"""Snake casing for methods"""

def name_of_function(name):
    print("Hello"+name)


def add_function(num1,num2):
    return num1+num2


def say_hello():
    print("hello")


name_of_function(" Baku")

def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello()

say_hello('Jolie')


def print_sum(num1,num2):
    print(num1+num2)


def return_sum(num1,num2):
    return num1+num2

print_sum(10,20)
print(return_sum(10,20))


