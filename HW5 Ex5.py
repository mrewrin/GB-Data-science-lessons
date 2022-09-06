def summury():
    try:
        with open('text_for_ex_5.txt', 'w+', encoding="utf-8") as txt_file:
            line = input("Please, enter your numbers through a space: \n")
            txt_file.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except IOError:
        print("File error!")
    except ValueError:
        print("Input-output error!")
summury()