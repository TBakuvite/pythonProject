def even_check(number):
    return number%2==0

print(even_check(21))

# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
def check_even_list(num_list):
    #return all the even numbers in a list
    even_numbers = []

    for number in num_list:
        if number%2==0:
            even_numbers.append(number)

        else:
            pass

    return even_numbers

print(check_even_list([1,3,5,8,10,12]))
print(check_even_list([1,3,5,7]))

