from itertools import count

my_list = count (111)

for _ in range(10):
    print("(my_list) = ({})".format (next (my_list)))
