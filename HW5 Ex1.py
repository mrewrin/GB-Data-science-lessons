new_file = open("test.txt", "w", encoding="utf-8")
lines = input("Please enter your text: \n")
while lines:
    new_file.write(lines + "\n")
    lines = input("Please enter your text: \n")
    if not lines:
        break

new_file.close()