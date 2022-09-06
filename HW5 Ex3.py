with open('text_for_ex3.txt', 'r', encoding="utf-8") as salary_mean:
    cow_dict = {line.split() [0]: float(line.split() [1]) for line in salary_mean}
    print(f'Coworkers earning less than 20000 {[e[0] for e in cow_dict.items() if e[1] < 20000]}. 'f'Total average salary = {round(sum(cow_dict.values()) / len(cow_dict), 3)}.')
