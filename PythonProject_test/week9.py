#수업 교안 내 예제
"""str = "Korea"
for i in str:
    print(i)

for i in [1, 2, 5, 7, 9]:
    print(i)"""

#애스터리스크로 직각 피라미드 만들기
"""for i in [1, 2, 3, 4, 5]:
    print("*" * i)

for i in range(1, 11, 2): # 1 3 5 7 9
    print("*" * i)"""

#3의 배수 전부 더하기
"""sum = 0
for i in range(0, 101, 3):
    sum += i
    print(i, sum)"""

#원하는 단의 구구단을 출력
"""dan = int(input("원하는 단을 입력하시오 >> "))
for i in range(9, 0, -1):
    print(f"{dan} * {i} = {dan * i}")"""

# 2 ~ 9 단 구구단 출력
"""for dan in range(2, 10):    # 2 ~ 9
    for i in range(1, 10):  # 1 ~ 9
        print(f"{dan} * {i} = {dan * i}")
    print()"""

# 몇 단부터 몇 단까지?
"""start = int(input("몇 단부터 시작할까요? >> "))
end = int(input("몇 단까지 할까요? >> "))
for i in range(start, end + 1):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print()"""

#원하는 단의 구구단을 정방향, 역방향으로
"""dan = int(input("출력할 단을 입력하시오 : "))
for i in range(1, 10):
    print(f"{dan} * {i} = {(dan * i):>2}   {dan} * {10 - i} = {dan * (10 - i):>2}")"""

#while문 이용해서 문장을 반복하기
"""count = 0
while count < 10:
    print(count)
    count += 1"""

# for, while로 1 ~ 10까지의 합을 구하는 프로그램
"""result = 0
for i in range(1, 11):
    result += i
print("for, 1에서 10까지의 합은", result)

total = 0
count = 1
while count <= 10:
    total += count
    count += 1
print("while, 1에서 10까지의 합은", total)"""

#random으로 로또 숫자 뽑기
"""import random

for i in range(6):  # 중복된 숫자가 나올 수 있어 좋지 않다
    number = random.randint(1, 45)
    print(number)


print("엔터키를 누르면 시작됩니다...")
input()

count = 0
list = []
while count < 7: # 중복된 숫자가 나올 경우 pass하는 while문이다.
    number = random.randint(1, 45)
    if number in list:
        pass
    else:
        list.append(number)
        count += 1

print(list)"""

