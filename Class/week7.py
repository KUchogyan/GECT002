#함수 선언하기
"""def myprint():
    print("=" * 20)
    print(" 고려대학교")
    print("=" * 20)

myprint()"""

#딕셔너리 이용해보기
cell_phone = {
    20190001 : ["Hong-gil-dong", "1992-01-02", "010-1111-2222"],
    20190002 : ["Lee-sun-shin", "1987-07-13", "010-6547-8755"],
    20190003 : ["Jang-bo-go", "1990-04-15", "010-3333-3555"]
}

print(cell_phone)
print(cell_phone.keys())
print(cell_phone.values())
print(cell_phone.items())

key = int(input("검색하고자 하는 학번 >> "))
if key in cell_phone.keys():
    print("존재하는 학번")
else:
    print("존재하지 않는 학번")

#:up 까지가 시험문제

name = input("검색하고자 하는 이름 >> ")
for key, value in cell_phone.items():
    if name in value:
        print("존재하는 이름입니다.")

        print(f"검색한 이름은 {value[0]}")
        print(f"생년월일은 {value[1]}")
        print(f"전화번호는 {value[2]}")
        print(f"학번은 {key}")