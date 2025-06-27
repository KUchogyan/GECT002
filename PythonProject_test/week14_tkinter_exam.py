from tkinter import *

window = None
title_label = None
entry_widget = None

def quit():
    window.destroy()

def entry_widget_func(event):
    global title_label, entry_widget
    title_label["text"] = entry_widget.get()
    entry_widget.delete(0, END)

def window_gui():
    global window, title_label, entry_widget
    window = Tk()
    window.title("My calc")
    #window.geometry("400x600")

    title_label = Label(window, text = "Korea University", relief = GROOVE, font = "TimeNewRoman 35 bold")
    title_label.grid(row=0, column=0)
    #title_label["text"] = "123456"

    quit_btn = Button(window, text="Quit", font="TimeNewRoman 20 bold", command=quit)
    quit_btn.grid(row = 0, column = 1)

    entry_widget = Entry(window, font="TimeNewRoman 12")
    entry_widget.grid(row = 1, column = 0)
    entry_widget.bind("<Return>", entry_widget_func)

window_gui()
window.mainloop()

