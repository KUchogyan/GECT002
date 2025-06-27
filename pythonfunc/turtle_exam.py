### turtle library를 import하기
import turtle as t


### 초기 선언 / 다양한 함수를 선언하기
t.shape('turtle')
t.color('green')

def step(n): # 명령어, 함수, 메서드
    for i in range(n):
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.left(90)

def square():
    for i in range(4):
        t.forward(100)
        t.right(90)

def mycircle():
    for i in range(150, 1, -10):
        t.circle(i)

def mycircle2():
    for c in ['crimson', 'green', 'blue', 'black']:
        t.right(90)
        t.color(c)
        for i in range(150, 1, -10):
            t.circle(i)


### 반복문과 함수로 사각형 그리기
"""for i in range(4):
    t.forward(100)
    t.right(90)"""

"""for i in range(4):
    t.left(90)
    t.forward(100)"""

#t.setheading(0)
#square()


### 반복문과 함수로 계단 그리기
"""for i in range(10):
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    step()"""

#step(5)


### 원 그리기
# 초기 속도 선언
t.speed(11)

#반복문과 간단한 나의 함수를 이용해 원 그리기
"""t.color('green')
for i in range(150, 1, -10):
    t.circle(i)

t.color('crimson')
t.setheading(270)
mycircle()

t.color('orange')
t.setheading(180)
mycircle()"""

#함수를 이용해 불필요한 부분을 많이 대체하기
"""t.setheading(0)
mycircle2()"""


### 선언한 함수를 연속으로 이용하기
"""mycircle2()
step(4)"""


### 방향키를 이용해 그림 그리기
#초기 설정
t.speed(11)

#각종 함수 선언
def move_left():
    t.setheading(180)
    t.forward(20)

def move_right():
    t.setheading(0)
    t.forward(20)

def move_up():
    t.setheading(90)
    t.forward(20)

def move_down():
    t.setheading(270)
    t.forward(20)

def move_circle():
    t.circle(70)

def color_crimson():
    t.color('crimson')

def color_green():
    t.color('green')

def color_blue():
    t.color('blue')

def pensize_sharp():
    t.pensize(1)

def pensize_middle():
    t.pensize(4)

def pensize_bold():
    t.pensize(8)

#함수가 잘 작동하는지 테스트
"""move_left()
move_right()
move_up()
move_down()"""

# 함수와 방향키를 연결하기
t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_circle, "0")
t.onkeypress(color_crimson, "1")
t.onkeypress(color_green, "2")
t.onkeypress(color_blue, "3")
t.onkeypress(pensize_sharp, "q")
t.onkeypress(pensize_middle, "w")
t.onkeypress(pensize_bold, "e")
t.listen()


t.done()    # turtle 윈도우의 종료버튼을 누를 때까지 대기