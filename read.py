text = ''

with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line

print(text)