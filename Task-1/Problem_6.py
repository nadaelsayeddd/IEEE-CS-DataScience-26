n = int(input())
lst = [n*i for i in range(11) if n*i % 4 != 0 ]
print(*lst)