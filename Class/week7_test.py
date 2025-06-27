#문제2-2
"""text = "Korea\nUniversity"

print(text)"""

#문제2-3
"""number = input("임의의 정수를 입력하십시오: ")

if number[-1] in "13579":
    print(f">> 입력한 {number}은 홀수 입니다.")
else:
    print(f">> 입력한 {number}은 짝수 입니다.")"""

#문제2-5
f = int(input('화씨 온도를 입력하세요 > '))
c = (f-32) * 5/9
print('>> 섭씨 온도는 {0:.1f}도 입니다.'.format(c))