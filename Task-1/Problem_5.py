n = int(input())
new_lst = [0, 1]
counter_1 = 0
for x in range(n - 2):
    new_lst.append(new_lst[counter_1 + 1] + new_lst[counter_1])
    counter_1 += 1
print(new_lst)

