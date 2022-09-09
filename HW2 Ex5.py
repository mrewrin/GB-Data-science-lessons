rating_list = [7, 5, 3, 3, 2]
print(f'Rating - {rating_list}')
n = int(input('Please, enter a new rating element from 1 to 998 or enter "999" for escape: '))
while n != 999:
    for el in range(len(rating_list)):
        if rating_list[el] == n:
            rating_list.insert(el + 1, n)
            break
        elif rating_list[0] < n:
            rating_list.insert(0, n)
        elif rating_list[-1] > n:
            rating_list.append(n)
        elif rating_list[el] > n > rating_list[el + 1]:
            rating_list.insert(el + 1, n)
    print(f"Rating list - {rating_list}")
    n = int(input("Please, enter a new rating element from 1 to 998: "))
