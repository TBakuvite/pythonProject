#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if(word.startswith('s')):
        print(word)

st = [word for word in st.split() if word.startswith('s')]
print(st)

#Use range() to print all the even numbers from 0 to 10
for num in range(0,10):
    if num%2==0:
        print(num)

numList = [num for num in range(0,10) if num%2==0]
print(numList)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
numList = [num for num in range(1,50) if num%3==0]
print(numList)

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word)


#Write a program that prints integers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for multiples of five print "Buzz". For numbers, which are multiples of both 3 and 5, print "FizzBuzz".
for num in range(1,100):
    if num%15==0:
        print(f'{num} FizzBuzz')
    elif num%3==0:
        print(f'{num} Fizz')
    elif num%5==0:
        print(f'{num} Buzz')


#Use list comprehension to create a list of the first letters of every word in the string below
st = 'Create a list of the first letters of every word in this string'
st = [word[0] for word in st.split()]
print(st)

