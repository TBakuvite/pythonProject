mylist = [1,2,3]

for num in range(10):
    print(num)


for num in range(3,10):
    print(num)

for num in range(0,10,2):
    print(num)

print(list(range(0,10,2)))


index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1


word = 'abcde'
for item in enumerate(word):
    print(item)


word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)


print(list(zip(mylist1,mylist2)))

print('x' in [1,2,3,4])

print('a' in 'Baku')

print('mykey' in {'mykey':35})

d = {'mykey':345}
print(345 in d.keys())

mylist = [10,20,30,40,100]
print(f'The smallest number in the list is {min(mylist)} and the biggest number is {max(mylist)}')
print('The biggest number is the list is {}'.format(max(mylist)))


from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))

result = input('Enter a number here: ')
print(result)

print(type(result))

print(float(result))



