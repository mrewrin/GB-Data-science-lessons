# rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new_file = []
# with open("text_for_ex4.txt", "r", encoding="utf-8") as before_translate:
#    for i in before_translate:
#        i = i.split(' ', 1)
#        new_file.append(rus[i[0]] + '  ' + i[1])
#    print(new_file)
#
#with open("file_4_new.txt", "w", encoding="utf-8") as after_translate:
#    after_translate.writelines(new_file)
# решение громоздкое, разобрал как работает решение, которое дали на 6м уроке, решил использовать его, как более элегантное

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open("text_for_ex4_final.txt", "w", encoding="utf-8") as secondary_file:
    with open("text_for_ex4.txt", encoding="utf-8") as primary_file:
        secondary_file.writelines([line.replace(line.split()[0], rus.get(line.split()[0])) for line in primary_file])

