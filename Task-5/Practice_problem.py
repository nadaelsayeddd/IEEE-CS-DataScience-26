import re
t = int(input())
for i in range(t):
    s = input()
    try:
        re.compile(s)
        if re.search(r'(?<![\\])[*+?][*+?]', s):
            print("False")
        else:
            print("True")
    except re.error:
        print("False")