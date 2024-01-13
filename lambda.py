def multiply_list_map(my_list=[], number = 0):
    return (list(map(lambda x: x * number, my_list)))

# return list(map(lambda x: x * number, my_list)):
# map(lambda x: x * number, my_list):
# Uses the map function to apply a transformation to each element in my_list:
# The lambda function lambda x: x * number takes an element x ...
#               from the list and multiplies it by the provided number.
# list(map(...)): Converts the results of the map function (an iterator) ...
#                   to a new list containing the transformed elements.

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 100)
print(new_list)
print(my_list)