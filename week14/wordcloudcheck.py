// 수업시간에 만든 워드클라우드 구현 프로그램
from konlpy.tag import Okt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

with open("todayhotnews.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
#print(text)

okt = Okt()
nouns_text = ''
for sentence in text:
    for noun in okt.nouns(sentence):
        if len(noun) < 2:
            pass
        elif noun in ["간다", "지금", "우려"]:
            pass
        elif noun == "이경규":
            nouns_text += "유길상" + " "
        else:
            nouns_text += noun + ' '
#print(nouns_text)

mask_image = np.array(Image.open("apple.jpg"))
wc = WordCloud(font_path = 'NanumSquareEB.ttf', background_color = "white", mask = mask_image,
               max_words = 250, max_font_size = 65, min_font_size = 10, colormap = "hsv").generate(nouns_text)
wc.to_file("todayhotnews.png")
