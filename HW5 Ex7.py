# что-то опять слишком громоздкое я наваял, фирма с убытком все равно выходит,
# а по итогу представленное решение на уроке 6 выглядит гораздо проще.
# Сдаю как есть, чтобы не затягивать со сдачей, ушел учить матчасть.
import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0

with open("text_7.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Profit average - {prof_aver:.2f}')
    else:
        print(f'Profit average - absent. Everyone works at a loss')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit per company - {profit}')

with open('text_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Created a json file with the following content: \n '
          f' {js_str}')