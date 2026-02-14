lst = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
nums = []
for _ in range(int(input())):
    commands = input().split()
    if commands[0] == lst[0]:
        nums.insert(int(commands[1]), int(commands[2]))
    elif commands[0] == lst[2]:
        nums.remove(int(commands[1]))
    elif commands[0] == lst[3]:
        nums.append(int(commands[1]))
    elif commands[0] == lst[4]:
        nums.sort()
    elif commands[0] == lst[5]:
        nums.pop()
    elif commands[0] == lst[6]:
        nums.reverse()
    if commands[0] == lst[1]:
        print(nums)