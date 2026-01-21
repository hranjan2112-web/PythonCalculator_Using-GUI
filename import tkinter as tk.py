import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

expression = ""

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear screen
def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()

# Display screen
screen = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, justify="right")
screen.grid(columnspan=4, ipadx=8)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (text,row,col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=equalpress).grid(row=row, column=col)
    elif text == "C":
        tk.Button(root, text=text, width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=row, column=col)

root.mainloop()
