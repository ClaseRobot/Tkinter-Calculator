from tkinter import *
import parser
from tkinter import font

# fondo #1B1E22
# boton igual #9481FD
# botones #2C2E33

window = Tk()

# window.geometry('600x400')
window.configure(bg = '#1B1E22')
window.title('Calculator')

# input fields
display = Entry(window)
display.grid(row=1, columnspan=6, sticky=W+E)

# Get Numbers to Display
i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except Exception:
        clear_display()
        display.insert(0, "Error")

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")

# Numeric Buttons
Button(window, text="1", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(1)).grid(row=2, column=0, sticky=W+E)
Button(window, text="2", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(window, text="3", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(window, text="4", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(window, text="5", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(window, text="6", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(window, text="7", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(window, text="8", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(8)).grid(row=4, column=1, sticky=W+E)
Button(window, text="9", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(9)).grid(row=4, column=2, sticky=W+E)

# Function Buttons

Button(window, text="AC", font="bold", bg="#9481FD", fg="#fff", height=2, command=lambda: clear_display()).grid(row=5, column=0, sticky=W+E)
Button(window, text="0", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(window, text="%", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_operation("%")).grid(row=5, column=2, sticky=W+E)

Button(window, text="+" , font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_operation("+")).grid(row=2, column=3, sticky=W+E)
Button(window, text="-", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_operation("-")).grid(row=3, column=3, sticky=W+E)
Button(window, text="*", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_operation("*")).grid(row=4, column=3, sticky=W+E)
Button(window, text="/", font="bold", bg="#2C2E33", fg="#fff", width=4, height=2, command=lambda: get_operation("/")).grid(row=5, column=3, sticky=W+E)

Button(window, text="⟵", font="bold", bg="#2C2E33", fg="#fff", height=2, command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(window, text="exp", font="bold", bg="#2C2E33", fg="#fff", height=2, command=lambda: get_operation("**")).grid(row=3, column=4, sticky=W+E)
Button(window, text="^2", font="bold", bg="#2C2E33", fg="#fff", height=2, command=lambda: get_operation("**2")).grid(row=3, column=5, sticky=W+E)
Button(window, text="(", font="bold", bg="#2C2E33", fg="#fff", height=2, command=lambda: get_operation("(")).grid(row=4, column=4, sticky=W+E)
Button(window, text=")", font="bold", bg="#2C2E33", fg="#fff", height=2, command=lambda: get_operation(")")).grid(row=4, column=5, sticky=W+E)
Button(window, text="=", font="bold", bg="#2C2E33", fg="#fff", height=2, command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan=2)

window.mainloop()