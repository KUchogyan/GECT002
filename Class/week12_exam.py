import turtle as t

t.shape('turtle')
t.speed(100)

color = ['red', 'orange', 'crimson', 'blue']

def draw_circles():
    global color
    for c in color:
        t.right(90)
        t.color(c)
        for i in range(140, 1, -10):
            t.circle(i)

def move_up():
    t.setheading(90)
    t.forward(20)

def move_down():
    t.setheading(270)
    t.forward(20)

def move_left():
    t.setheading(180)
    t.forward(20)

def move_right():
    t.setheading(0)
    t.forward(20)

t.onkeypress(move_left, "Left")
t.onkeypress(move_right, "Right")
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(draw_circles, "0")

t.listen()

t.done()
