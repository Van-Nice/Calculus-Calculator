import tkinter as tk
import math
from sympy import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import latexify as lt


# Constants
PI = math.pi
E = math.e

calculation = ""

def get_calculation():
    return calculation

# live matplotlib section
def live_calculation():
    calculation_in_latex = lt.get_latex(get_calculation())
    print(calculation_in_latex)
    return calculation_in_latex

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# hashmap for output

root = tk.Tk()
root.geometry("500x425")

# set up grid
text_result = tk.Text(root, height=5, width=32, font=("Arial", 24))
text_result.grid(columnspan=5)

# First Row
# Button /
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=1, column=4)
# Button ^
btn_power_of = tk.Button(root, text="^", command=lambda: add_to_calculation("**"), width=5, font=("Arial", 14))
btn_power_of.grid(row=1, column=1)
# Button ln "Base e"
btn_ln = tk.Button(root, text="ln", command=lambda: add_to_calculation("math.log("), width=5, font=("Arial", 14))
btn_ln.grid(row=1, column=2)
# Button π
btn_pi = tk.Button(root, text="π", command=lambda: add_to_calculation("π"), width=5, font=("Arial", 14))
btn_pi.grid(row=1, column=3)
# Button e
btn_pi = tk.Button(root, text="e", command=lambda: add_to_calculation("math.e"), width=5, font=("Arial", 14))
btn_pi.grid(row=1, column=4)
# Second Row

# Button 1
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
# Button 2
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
# Button 3
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
# Button +
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)


# Third Row
# Button 4
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
# Button 5
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
# Button 6
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
# Button -
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

# Fourth Row

# Button 7
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
# Button 8
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
# Button 9
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
# Button *
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)

# Fifth Row

# Button 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=1)
# Button .
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=5, column=2)
# Button (
btn_first_parenthesis = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_first_parenthesis.grid(row=5, column=3)
# Button )
btn_second_parenthesis = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_second_parenthesis.grid(row=5, column=4)

# Sixth Row
# Button Clear
btn_clear = tk.Button(root, text="CLEAR", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1)
# Button Equals
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
btn_equals.grid(row=6, column=2)

root.mainloop()