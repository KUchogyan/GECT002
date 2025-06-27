#연산순서: 산 - 관 - 논
"""x = 5
y = 10
print(x > y)
print(x < y)

print(x == y)
print(x != y)"""

#나이 구별 프로그램1
"""age = int(input("당신의 나이를 입력하세요: "))
print(age >= 19 and age < 60)
print(19 <= age <60)

if 19 <= age < 60:
    print("입장 가능한 연령입니다.")
else:
    print("입장 불가능한 나이 입니다.")"""

#나이 구별 프로그램2
"""age = int(input("나이 입력: "))
print(age < 10 or age >= 70)

if age < 10 or age >= 70:
    print("교통약자석을 이용할 수 있는 나이입니다.")
else:
    print("교통약자를 배려해주시기 바랍니다.")"""

#논리 연산자 not 사용해보기
"""A = int(input("press any number..."))
result = not A
print(result)"""

#if를 이용한 프로그램
'''print(
"""==========
 홍 대 클 럽
==========""")

age = int(input("실례지만 나이가 어떻게 되시는지요?.."))
if age > 24:
    print("죄송합니다만, 오늘은 입장 불가하십니다")
    print("다음에 뵙기를 고대하겠습니다")
if age <= 24:
    print("어서 오십시오")
'''

#연습문제1
"""score = int(input("Please enter your Score : "))

if(score >= 60):
    print("Pass")
else:
    print("Fail")"""

#연습문제2
"""score = int(input("Enter your score > "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif 0 <= score <= 59:
    print("F")
else:
    print("Wrong Score")"""

#연습문제3-1
"""number = int(input("Please enter any number > "))

if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")"""

#연습문제3-2
"""number = input("Enter any number > ")

if number[-1] in "02468":
    print("Even number.")
else:
    print("Odd number.")"""

#연습문제3-3
"""number = int(input("Enter any number > "))

print("Odd.") if number % 2 == 1 else print("Even.")

print("Odd" if number % 2 ==1 else "Even")

#print("Odd" if number[-1] in '13579' else "Even")"""

#양수, 음수, 0을 체크하는 프로그램
number = int(input("Enter any number > "))
if number > 0:
    print("it's positive number.")
elif number < 0:
    print("it's negative number.")
else:
    print("it's zero.")

