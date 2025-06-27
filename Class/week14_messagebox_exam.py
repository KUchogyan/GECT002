from tkinter import messagebox

a = 12312
b = 44556
c = a + b
#print("두 수의 합", c)
messagebox.showinfo("두 수의 합", c)

ans = messagebox.askyesno("질문", "Are you a freshman?")
if ans:
    messagebox.showinfo("Alert", "Welcome!")
else:
    messagebox.showerror("Warning", "You can't...")