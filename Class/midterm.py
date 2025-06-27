#4th problem
"""age = int(input("나이를 입력하세요"))

if 9 <= age <= 24:
    print("청소년입니다.")
else:
    print("청소년이 아닙니다.")"""

#5th problem
#number = input("숫자를 입력하시오 >> ")
#print("홀수 입니다." if number[-1] in "13579" else "짝수 입니다")

#6th problem
"""word = input("단어를 입력하세요")
print(word[::-1])"""

#7th problem
cell_phone_db = {'홍길동': ['010-5656-5656', '1995-08-21'],
                       '이순신': ['021-3213-4212', '1805-12-11'],
                       '장보고': ['132-4323-43242', '2001-01-01']}

name = input('검색하고자 하는 이름을 입력하세요 >')
if ( name in cell_phone_db):
    print(f"{name}님의 정보는 다음과 같습니다. {cell_phone_db[name]}")
else:
    print(f'{name}님의 정보는 없습니다.')