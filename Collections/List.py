my_list = [1.5,'Baku','three',1345]
print(my_list[0])
another_list = ['four','five']
print(my_list+another_list)
print(my_list[1:])
new_list = my_list+another_list
print(new_list)
new_list[0] = 3.5
print(new_list)
new_list.append('BMW')
print(new_list)
new_list.pop()
print(new_list)
popped_item = new_list.pop()
print(popped_item)
print(new_list.pop((0)))
print(new_list)
new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]
new_list.sort() #sort is a void method
print(new_list)
num_list.reverse()
print(num_list)
print(num_list[1:])
