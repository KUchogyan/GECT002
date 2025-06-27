#인수를 받는 함수 만들어보기
'''def my_print(count):
    for i in range(count):
        print("""
==================
 Korea University
==================""")

my_print(10)'''

#입력받는 값의 수가 가변적인 함수 만들어보기
"""def hap(*many):
    h = 0
    for i in many:
        h += i
    return h


result = hap(1, 2, 3, 4, 5, 6)
print("합계:", result)

result = hap(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("합계:", result)"""

# list가 인자인 함수 만들기
"""def hap(list):
    h = 0
    for i in list:
        h += i
    return h

a = [1, 2, 3, 4, 5, 6]
result = hap(a)
print("합계:", result)"""