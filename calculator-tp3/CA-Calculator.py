import tkinter as tk

def click_button(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(value))

def evaluate():
    try:
        current_expression = entry.get()
        
        # Replace 'x' with '*' for multiplication
        current_expression = current_expression.replace('x', '*')
        
        result = eval(current_expression)
        
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Handle division by zero
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Handle any other errors

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: click_button(value))
    
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
