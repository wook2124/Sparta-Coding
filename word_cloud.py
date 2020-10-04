from wordcloud import WordCloud

text = ''

with open("KaKaoTalk 2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '').replace('이모티콘\n', '').replace('사진\n', '').replace('ㅇ', '').replace('ㅎ', '')

# print(text)

wc = WordCloud(font_path='C:/Users/wook2/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothicBold.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

# # 폰트가 저장된 위치 확인하기
# import matplotlib.font_manager as fm

# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)