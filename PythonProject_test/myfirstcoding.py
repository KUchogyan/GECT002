import math
print("""
==========
원의 둘레와 면적 계산기
==========""")

rad = float(input("반지름을 입력해 주세요 > "))   #키보드로 데이터 직접 입력받기
pi = math.pi

length = 2 * pi * rad
space = pi * rad * rad

print("반지름 :", rad)
print("원의 둘레는", length, "입니다")
print("원의 면적은", space, "입니다")
