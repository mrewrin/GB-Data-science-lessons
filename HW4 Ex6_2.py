from itertools import cycle

my_list = cycle ("ABC")

for _ in range (10):
    print("(my_list) = ({})".format (next (my_list)))
