s = input().lower()

vowels = "aeiou"
res = [s.count(ch) for ch in vowels if ch in s]

print(sum(res))