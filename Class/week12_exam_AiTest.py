import turtle as t
import time
t.shape('turtle')
t.speed(100)

colors = ['red', 'orange', 'crimson', 'blue']
current_color = 'red'  # Starting color
radius = 50  # Initial radius

def draw_circles():
    t.color(current_color)
    t.circle(radius)

def change_color():
    global current_color
    current_index = colors.index(current_color)
    current_color = colors[(current_index + 1) % len(colors)]
    t.color(current_color)
    t.write(f"Color: {current_color}", font=("Arial", 12, "normal"))
    time.sleep(0.5)  # Wait for 0.5 seconds
    t.undo()  # Remove the text after delay

def increase_radius():
    global radius
    radius = min(radius + 10, 200)  # Maximum radius of 200
    t.write(f"Radius: {radius}", font=("Arial", 12, "normal"))
    time.sleep(0.5)  # Wait for 0.5 seconds
    t.undo()  # Remove the text after delay

def decrease_radius():
    global radius
    radius = max(radius - 10, 10)  # Minimum radius of 10
    t.write(f"Radius: {radius}", font=("Arial", 12, "normal"))
    time.sleep(0.5)  # Wait for 0.5 seconds
    t.undo()  # Remove the text after delay

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
t.onkeypress(draw_circles, "space")
t.onkeypress(increase_radius, "equal")  # = key
t.onkeypress(decrease_radius, "minus")  # - key
t.onkeypress(change_color, "c")  # c key for color change

t.listen()

t.done()