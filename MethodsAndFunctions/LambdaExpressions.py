def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']

print(list(map(splicer,names)))


def check_even(num):
    return num%2==0

print(check_even(6))

mynums = [1,2,3,4,5,6]

print(list(filter(check_even,mynums)))

for n in filter(check_even,mynums):
    print(n)


def square(num):
    return num**2

square = lambda num: num**2

print(square(6))

print(list(map(lambda num:num**2,mynums)))

print(list(filter(lambda num:num%2==0,mynums)))

print(names)

print(list(map(lambda x:x[0],names)))