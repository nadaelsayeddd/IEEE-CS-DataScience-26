records = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
    scores.append(score)

scores_set = sorted(set(scores))
second = scores_set[1]

names_lst = [record[0] for record in records if record[1] == second]
names_lst.sort()

for name in names_lst:
    print(name)


