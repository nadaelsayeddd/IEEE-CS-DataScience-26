n = int(input())
A = list(map(int, input().split()))

new_a = sorted(set(A))

print(new_a[-2])