from konlpy.tag import Okt
myOkt = Okt()

### konlpy 이용해보기
# Okt 이용해보기
"""from konlpy.tag import Okt
myOkt = Okt()

myOkt.nouns("아버지가 방에 들어갑니다.")

text = "아버지가 방에 들어갑니다."
myOkt.morphs(text)
myOkt.pos(text)"""

# Kkma 이용해보기
"""from konlpy.tag import Kkma

myKkma = Kkma()

print(myKkma.nouns(text))
print(myKkma.pos(text))"""

### 댓글을 분석해보기
## 줄 단위로 분석하기
with open("frozen2_movie.txt") as f:
    text = f.readlines()
#print(text)

## 그 줄의 명사를 분석하기
bucket_list = []
for line in text:
    bucket_list.extend(myOkt.nouns(line))
#print(bucket_list)

## 명사 모음의 빈도수를 분석하기
from collections import Counter
counter = Counter(bucket_list)
#print(counter)

## 빈도수 상위 50개만 출력
#print(counter.most_common())