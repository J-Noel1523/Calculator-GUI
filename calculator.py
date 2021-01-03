from tkinter import *

root = Tk()
root.title("Calculator App")

def clear():
    user_input.delete(0, END)

def click(number):
    curr = user_input.get()
    user_input.delete(0, END)
    user_input.insert(0, f"{curr}{number}")

def add():
    current = user_input.get()
    global curr
    curr = int(current)
    global operation
    operation = "add"
    user_input.delete(0, END)

def subtract():
    current = user_input.get()
    global curr
    curr = int(current)
    global operation
    operation = "sub"
    user_input.delete(0, END)

def multiply():
    current = user_input.get()
    global curr
    curr = int(current)
    global operation
    operation = "mult"
    user_input.delete(0, END)

def divide():
    current = user_input.get()
    global curr
    curr = int(current)
    global operation
    operation = "div"
    user_input.delete(0, END)

def equal():
    current_2 = user_input.get()
    global curr_2
    curr_2 = int(current_2)
    user_input.delete(0, END)
    
    if operation == "add":
        user_input.insert(0, curr + curr_2)
    elif operation == "sub":
        user_input.insert(0, curr - curr_2)
    elif operation == "mult":
        user_input.insert(0, curr * curr_2)
    elif operation == "div":
        try:
            user_input.insert(0, curr / curr_2)
        except:
            print("Cannot divide by zero")
            user_input.insert(0, "Cannot divide by zero")
    else:
        user_input.insert(0, 'Error')
    
user_input = Entry(root, width=35, borderwidth=5)
user_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_subtract = Button(root, text="-", padx=40, width=1, pady=20, command=subtract)
button_multiply = Button(root, text="x", padx=40, pady=20, command=multiply)
button_divide = Button(root, text="÷", padx=39, pady=20, command=divide)
button_equal = Button(root, text="=", padx=37, width=29, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=33, width=3, pady=20, command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=4, column=2)
button_equal.grid(row=6, column=0, columnspan=3)
button_clear.grid(row=4, column=0)

button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

root.mainloop()