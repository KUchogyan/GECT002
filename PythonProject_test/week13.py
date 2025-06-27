### try split()
"""date = "2025.06.02"
date_list = date.split(".")
print(date_list)"""

### Test 1
"""scores = input("여러 개의 점수를 입력하시오 >").split(" ")
for i in range(len(scores)):
    scores[i] = int(scores[i])
print(sum(scores))"""

### Test 2
"""'''def f(x):
    return x ** 2'''

f = lambda x: x ** 2
print(f(3))"""

### Test 3
"""with open("alice_assignment.txt") as f:
    text = f.read()

print("총글자수:", len(text))
print("총단어수:", len(text.split(" ")))
print("라인수:", len(text.split("\n")))"""

### Test 4
'''while(1):
    print("""---------------------
    2025 뉴 가위 바위 보 게임
    ---------------------""")'''