### 지역변수와 전역변수 이해하기
"""def c():
    a = 1
    print(a)

def y():
    global a
    print(a)

a = 3
c()
y()
print(a)"""

### .split() 사용해보기
"""def hap(bigdata):
    sum = 0
    for i in bigdata:
        sum += i
    return sum

jumsu = input("여러 개의 점수를 입력하세요 >> ").split()

# 문자로 입력받은 리스트의 값을 정수형으로 바꾸기
new_list = []
for i in jumsu:
    new_list.append(int(i))

# 오리지널 버전으로 출력 \n 정수형으로 바꾼 버전으로 출력
print(jumsu)
print(new_list)

total = hap(new_list)
print(total)"""

### 합계를 구하는 함수 이용해보기
data = [12, 23, 34, 45, 56]

print(sum(data))
