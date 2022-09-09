from functools import reduce
def my_function(el_p, el):
    return el_p * el
print(f'List of even values {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'The result of multiplying all elements of the list {reduce(my_function, [el for el in range(99, 1001) if el % 2 == 0])}')
