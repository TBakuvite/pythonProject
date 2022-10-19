x = 25
def printer():
    x=50
    return x

print(x)


name = 'THIS IS A GLOBAL STRING'
def greet():
    name = 'Sammy'
    def hello():
        print('Hello '+name)
    hello()

greet()
