from wordcloud import WordCloud

text = ''

with open("KaKaoTalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line

wc = WordCloud(font_path='C:/Users/wook2/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothicBold.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

# # 폰트 위치 알아내기
# import matplotlib.font_manager as fm

# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)