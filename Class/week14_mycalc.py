from tkinter import *

window = None
display_label = None
expression = ""

def press(n):
    global expression
    global display_label
    expression += n
    display_label["text"] = expression

def press_result():
    global expression
    global display_label
    try:
        display_label["text"] = str(round(eval(expression), 14))
    except:
        display_label["text"] = "Error"
    expression = ""

def press_clear():
    global expression
    global display_label
    expression = ""
    display_label["text"] = expression

def press_backspace():
    global expression
    global display_label
    expression = expression[:-1]
    display_label["text"] = expression

def press_square():
    global expression
    global display_label
    expression += "**2"
    display_label["text"] = expression


def window_gui():
    global window
    global display_label
    global expression

    window = Tk()
    window.title("박서현")

    display_label = Label(window, text="0", anchor="e", relief=SUNKEN, width=15, font="Arial 20")
    display_label.grid(row=0, column=0, columnspan=4)

    btn0 = Button(window, text="0", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("0"))
    btn1 = Button(window, text="1", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("1"))
    btn2 = Button(window, text="2", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("2"))
    btn3 = Button(window, text="3", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("3"))
    btn4 = Button(window, text="4", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("4"))
    btn5 = Button(window, text="5", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("5"))
    btn6 = Button(window, text="6", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("6"))
    btn7 = Button(window, text="7", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("7"))
    btn8 = Button(window, text="8", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("8"))
    btn9 = Button(window, text="9", width=5, height=2, font="TimeNewRoman 15 bold", command=lambda: press("9"))
    btn0.grid(row=5, column=1)
    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)

    clear_btn   = Button(window, text="C", width=5, height=2, font="TimeNewRoman 15", command=press_clear)
    result_btn  = Button(window, text="=", width=5, height=2, font="TimeNewRoman 15", command=press_result)
    add_btn     = Button(window, text="+", width=5, height=2, font="TimeNewRoman 15", command=lambda: press("+"))
    sub_btn     = Button(window, text="-", width=5, height=2, font="TimeNewRoman 15", command=lambda: press("-"))
    mul_btn     = Button(window, text="×", width=5, height=2, font="TimeNewRoman 15", command=lambda: press("*"))
    div_btn     = Button(window, text="÷", width=5, height=2, font="TimeNewRoman 15", command=lambda: press("/"))
    clear_btn   .grid(row=1 ,column=0)
    result_btn  .grid(row=5 ,column=2)
    add_btn     .grid(row=2 ,column=3)
    sub_btn     .grid(row=3 ,column=3)
    mul_btn     .grid(row=4 ,column=3)
    div_btn     .grid(row=5 ,column=3)

    backspace_btn   = Button(window, text="←", width=5, height=2, font="TimeNewRoman 15", command=press_backspace)
    percentage_btn  = Button(window, text="%", width=5, height=2, font="TimeNewRoman 15", command=lambda: press("*0.01"))
    square_btn      = Button(window, text="X²", width=5, height=2, font="TimeNewRoman 15", command=press_square)
    decimal_btn     = Button(window, text=".", width=5, height=2, font="TimeNewRoman 15", command=lambda: press("."))
    backspace_btn   .grid(row=1, column=1)
    percentage_btn  .grid(row=1, column=2)
    square_btn      .grid(row=1, column=3)
    decimal_btn     .grid(row=5, column=0)


window_gui()
window.mainloop()