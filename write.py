f = open("test.txt", "w", encoding="utf-8")
f.write("안녕, 스파르타!\n")

for i in [1, 2, 3, 4, 5]:
    f.write(f"{i}번째 줄이에요\n")

f.close()