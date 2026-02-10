s = input()
lst = s.split(" ")
longest = ""
for word in lst:
    if len(word) > len(longest):
        longest = word

print(f"The longest word is: {longest}")
