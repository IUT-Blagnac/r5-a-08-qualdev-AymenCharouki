from behave import given, when, then
import tkinter as tk

context = {}

@given('the calculator is open')
def step_impl(context):
    context.root = tk.Tk()
    context.entry = tk.Entry(context.root)
    context.entry.pack()

    context.buttons = {
        '7': tk.Button(context.root, text="7", command=lambda: context.entry.insert(tk.END, '7')),
        '8': tk.Button(context.root, text="8", command=lambda: context.entry.insert(tk.END, '8')),
        '9': tk.Button(context.root, text="9", command=lambda: context.entry.insert(tk.END, '9')),
        '4': tk.Button(context.root, text="4", command=lambda: context.entry.insert(tk.END, '4')),
        '5': tk.Button(context.root, text="5", command=lambda: context.entry.insert(tk.END, '5')),
        '6': tk.Button(context.root, text="6", command=lambda: context.entry.insert(tk.END, '6')),
        '1': tk.Button(context.root, text="1", command=lambda: context.entry.insert(tk.END, '1')),
        '2': tk.Button(context.root, text="2", command=lambda: context.entry.insert(tk.END, '2')),
        '3': tk.Button(context.root, text="3", command=lambda: context.entry.insert(tk.END, '3')),
        '0': tk.Button(context.root, text="0", command=lambda: context.entry.insert(tk.END, '0')),
        '+': tk.Button(context.root, text="+", command=lambda: context.entry.insert(tk.END, '+')),
        '-': tk.Button(context.root, text="-", command=lambda: context.entry.insert(tk.END, '-')),
        'x': tk.Button(context.root, text="x", command=lambda: context.entry.insert(tk.END, '*')),  
        '/': tk.Button(context.root, text="/", command=lambda: context.entry.insert(tk.END, '/')),
        '=': tk.Button(context.root, text="=", command=lambda: evaluate(context)),
        'C': tk.Button(context.root, text="C", command=lambda: context.entry.delete(0, tk.END)),
    }

    for button in context.buttons.values():
        button.pack()

    context.root.update_idletasks()

@when('I enter "{value}"')
def step_impl(context, value):
    context.entry.insert(tk.END, value)

@when('I press "{button}"')
def step_impl(context, button):
    context.buttons[button].invoke() 

@then('the result should be "{result}"')
def step_impl(context, result):
    assert context.entry.get() == result

@then('the input should be empty')
def step_impl(context):
    assert context.entry.get() == "", f"Expected input to be empty, but got: {context.entry.get()}"


def evaluate(context):
    try:
        expression = context.entry.get()
        result = str(eval(expression))  
        context.entry.delete(0, tk.END)
        context.entry.insert(tk.END, result) 
    except Exception as e:
        context.entry.delete(0, tk.END)
        context.entry.insert(tk.END, "Error")
