# 4번 문제
"""for dan in range(2, 10):
    for i in range(1, 10):
        print(f" {dan} x {i} = {dan * i:>2}")
    print()"""

#5번 문제
import random

print("""---------------------------------------
컴퓨터가 알려주는 행운의 로또번호
---------------------------------------""")
input("아무키나 누르면 추첨을 시작합니다.")

count = 0
list = []
while count < 6:
    number = random.randint(1, 46)
    if number in list:
        pass
    else:
        list.append(number)
        count += 1

print(f"이번주 행운의 번호는 {list} 입니다.")

#2번 문제
"""sum = 0
for i in range(99, 0, -2):
    sum += i
print("Sum :", sum)"""