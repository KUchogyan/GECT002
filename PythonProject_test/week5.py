#문자열 서식을 이용해 변수 출력하기
"""a = "koera"
b = "university"
print("%12s" % a)
print("%12s" % b)
print("대학교 이름은 %s %s입니다." % (a, b))

c = 2345.34657
print("%12.2f" % c)"""

#문자열 포맷 함수를 이용하여 출력하기
"""name = input("당신의 이름은? ")
age = int(input("당신의 나이: "))

print("당신의 이름은 {}이고 당신의 나이는 {}살 입니다." .format(name, age))
print("당신의 이름은 {0:}이고 당신의 나이는 {1:}살 입니다." .format(name, age))
print("당신의 이름은 {1:}이고 당신의 나이는 {0:}살 입니다." .format(name, age))
print("당신의 이름은 {1:}이고 당신의 나이는 {1:}살 입니다." .format(name, age))

print(f"당신의 이름은 {name}이고 당신의 나이는 {age}살 입니다.")"""

#문자열을 정렬하여 출력하기
"""파이값 = 3.141592
이름 = "홍길동"

#print(f"파이값은 {파이값}입니다.")
print("파이값은 {0:^15.1f}입니다.".format(파이값))
print("이름은 {0:>15s}입니다.".format(이름))
print("이름은 {0:<15s}입니다.".format(이름))
print("이름은 {0:^15s}입니다.".format(이름))
print(f"이름은 {이름:>15s}입니다.")"""

#실습문제; 학번 분리하기
"""fullStudentNumber = input("학번을 입력하세요 >> ")

entryYear = fullStudentNumber[0:4]
studentNumber = fullStudentNumber[4:10]

print(f"입학년도:{entryYear:>10s}")
print(f"학생번호:{studentNumber:>10s}")

#advanced...
print("입학년도:%10s" % fullStudentNumber[:4])
print("학생번호:%10s" % fullStudentNumber[4:])"""

#실습문제; 화씨 온도를 섭씨 온도로 바꾸기
"""f = int(input("화씨를 입력해주세요: "))
c = (f - 32) * 5 / 9

print("입력한 {0:}화씨 온도는 섭씨 온도로는 {1:.2f}입니다.".format(f, c))
print(f"입력한 화씨 {f}온도는 섭씨 온도로는 {c:.2f}입니다.")"""