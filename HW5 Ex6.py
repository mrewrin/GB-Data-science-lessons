subj = {}
with open("text_6.txt", encoding="utf-8") as file:
    for line in file:
        names, stats = line.split(":")
        names_sum = sum(map(float, "".join([i for i in stats if i == " " or "9" >= i >= "0"]).split()))
        subj[names] = names_sum
    print(f'Total number of hours per subject: \n {subj}')