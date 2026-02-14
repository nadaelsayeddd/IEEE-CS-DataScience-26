with open(r"c:\Users\Nada\Downloads\simple_text.txt") as f:
    txt = f.read()
words = txt.split()
lst = []
for word in words:
    new_word = word.replace(",", "")
    lst.append(new_word)

count = 0
for i in lst:
    if len(i) > 5:
        count+=1
print(count)
