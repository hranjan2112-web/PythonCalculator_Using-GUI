import tkinter as tk
import math

# ---------------- GLOBAL STATE ---------------- #
memory = 0
is_degree = True

# ---------------- CORE FUNCTIONS ---------------- #
def insert(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def backspace():
    display.delete(len(display.get())-1, tk.END)

def toggle_angle():
    global is_degree
    is_degree = not is_degree
    angle_btn.config(text="DEG" if is_degree else "RAD")

def evaluate():
    try:
        expr = display.get()
        expr = expr.replace("^", "**")
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        history.insert(tk.END, f"{expr} = {result}\n")
        clear()
        display.insert(0, result)
    except:
        clear()
        display.insert(0, "Error")

# ---------------- SCIENTIFIC ---------------- #
def trig(func):
    try:
        value = float(display.get())
        clear()
        if is_degree:
            value = math.radians(value)
        result = getattr(math, func)(value)
        display.insert(0, result)
    except:
        display.insert(0, "Error")

def factorial():
    try:
        value = int(display.get())
        clear()
        display.insert(0, math.factorial(value))
    except:
        display.insert(0, "Error")

def npr():
    try:
        n, r = map(int, display.get().split(","))
        clear()
        display.insert(0, math.perm(n, r))
    except:
        display.insert(0, "Error")

def ncr():
    try:
        n, r = map(int, display.get().split(","))
        clear()
        display.insert(0, math.comb(n, r))
    except:
        display.insert(0, "Error")

# ---------------- MEMORY ---------------- #
def memory_add():
    global memory
    memory += float(display.get())

def memory_sub():
    global memory
    memory -= float(display.get())

def memory_recall():
    clear()
    display.insert(0, memory)

def memory_clear():
    global memory
    memory = 0

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("460x620")
root.resizable(False, False)

display = tk.Entry(root, font=("Consolas", 18), bd=8, relief=tk.RIDGE, justify="right")
display.pack(fill=tk.X, padx=10, pady=10)

# History
history = tk.Text(root, height=6, font=("Consolas", 10))
history.pack(fill=tk.X, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(expand=True, fill="both")

buttons = [
    ("7","8","9","/","C"),
    ("4","5","6","*","⌫"),
    ("1","2","3","-","^"),
    ("0",".","=","+","%"),
]

for row in buttons:
    r = tk.Frame(btn_frame)
    r.pack(expand=True, fill="both")
    for b in row:
        cmd = (
            evaluate if b=="=" else
            clear if b=="C" else
            backspace if b=="⌫" else
            lambda x=b: insert(x)
        )
        tk.Button(r, text=b, font=("Arial",14), command=cmd)\
            .pack(side="left", expand=True, fill="both")

# Scientific Panel
sci = tk.Frame(root)
sci.pack(fill="both")

angle_btn = tk.Button(sci, text="DEG", command=toggle_angle)
angle_btn.grid(row=0, column=0)

tk.Button(sci, text="sin", command=lambda: trig("sin")).grid(row=0, column=1)
tk.Button(sci, text="cos", command=lambda: trig("cos")).grid(row=0, column=2)
tk.Button(sci, text="tan", command=lambda: trig("tan")).grid(row=0, column=3)

tk.Button(sci, text="!", command=factorial).grid(row=1, column=0)
tk.Button(sci, text="nPr", command=npr).grid(row=1, column=1)
tk.Button(sci, text="nCr", command=ncr).grid(row=1, column=2)
tk.Button(sci, text="√", command=lambda: insert("math.sqrt(")).grid(row=1, column=3)

tk.Button(sci, text="π", command=lambda: insert(str(math.pi))).grid(row=2, column=0)
tk.Button(sci, text="e", command=lambda: insert(str(math.e))).grid(row=2, column=1)
tk.Button(sci, text="|x|", command=lambda: insert("abs(")).grid(row=2, column=2)

# Memory
mem = tk.Frame(root)
mem.pack(fill="both")

tk.Button(mem, text="M+", command=memory_add).pack(side="left", expand=True, fill="both")
tk.Button(mem, text="M-", command=memory_sub).pack(side="left", expand=True, fill="both")
tk.Button(mem, text="MR", command=memory_recall).pack(side="left", expand=True, fill="both")
tk.Button(mem, text="MC", command=memory_clear).pack(side="left", expand=True, fill="both")

root.mainloop()
