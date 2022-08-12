test_list = input("Please enter list elements: ").split()
for i in range(0, len(test_list) - 1, 2):
    test_list[i], test_list[i + 1] = test_list[i + 1], test_list[i]
print(test_list)
