### math library 설명
"""#from math import sqrt, factorial
import math
print(dir(math))

print(math.factorial(5))
print(math.sqrt(16))"""

# 더하기 게임 만들기
"""import random
xo = 'o'
lv = 0

while xo == 'o':
    x = random.randint(1, 9 + lv)
    y = random.randint(1, 9 + lv)

    print(f"문제 {lv+1}")
    answer = int(input(f"{x} + {y} = "))

    if answer == x + y:
        print("정답입니다.\n")
        lv += 1
    else:
        print("오답입니다.")
        xo = 'x'"""

# random.choice() 사용해보기
"""import random

menu = ['pizza', 'tteokbokki', 'cafeteria', 'ramyeon', 'hamburger', 'sushi', 'noodle']
print(f"I recommend {random.choice(menu)}.")"""

# 가위바위보 게임 만들어보기
import random

win = "win"
while win == "win":
    print("""---------------------
2025 뉴 가위 바위 보 게임
---------------------""")

    computer_choice = random.choice(["가위", "바위", "보"])
    player_choice = input("가위 바위 보 중에서 하나를 입력하세요 >> ")
    print(f"컴퓨터: {computer_choice} / 플레이어: {player_choice}")

    if player_choice == computer_choice:
        print("비겼습니다.\n")
    elif (player_choice == "가위" and computer_choice == "보") or (player_choice == "바위" and computer_choice == "가위") or (player_choice == "보" and computer_choice == "바위"):
        print("😃플레이어가 이겼습니다.\n")
    else:
        print("플레이어가 졌습니다.😭😭")
        win = "lose"


# random library의 shuffle() 이용해보기
"""import random

list = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(list)

print(list)"""

# random library의 choices() 이용해보기
"""import random

input("추첨을 통해 경품을 드립니다.\n준비가 되셨다면 엔터키를 누르세요.")
product = ["Pocket tissues", "$10 Voucher", "Starbucks Gifticon", "$50 Voucher", "iPad 5th generation"]

lucky_box = random.choices(product, weights = [50, 30, 11, 8, 1], k = 1)
print("Congratulations! You got %s!!" % lucky_box)"""