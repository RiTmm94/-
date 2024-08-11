import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)



window = tk.Tk()

window.title('Ярин калькулятор')

window.geometry('600x400')

window.configure(bg='lightblue')

window.resizable(False, False)

button_add = tk.Button(window, text='+', width=4, height=2, command=add)
button_add.place(x=50, y=200)
button_sub = tk.Button(window, text='-', width=4, height=2, command=sub)
button_sub.place(x=110, y=200)
button_mul = tk.Button(window, text='*', width=4, height=2, command=mul)
button_mul.place(x=170, y=200)
button_div = tk.Button(window, text='/', width=4, height=2, command=div)
button_div.place(x=230, y=200)

button_1 = tk.Button(window, text='1', width=6, height=3)
button_1.place(x=330, y=50)
button_2 = tk.Button(window, text='2', width=6, height=3)
button_2.place(x=410, y=50)
button_3 = tk.Button(window, text='3', width=6, height=3)
button_3.place(x=490, y=50)
button_4 = tk.Button(window, text='4', width=6, height=3)
button_4.place(x=330, y=140)
button_5 = tk.Button(window, text='5', width=6, height=3)
button_5.place(x=410, y=140)
button_6 = tk.Button(window, text='6', width=6, height=3)
button_6.place(x=490, y=140)
button_7 = tk.Button(window, text='7', width=6, height=3)
button_7.place(x=330, y=230)
button_8 = tk.Button(window, text='8', width=6, height=3)
button_8.place(x=410, y=230)
button_9 = tk.Button(window, text='9', width=6, height=3)
button_9.place(x=490, y=230)
button_0 = tk.Button(window, text='0', width=6, height=3)
button_0.place(x=410, y=320)



number1_entry = tk.Entry(window, width=36)
number1_entry.place(x=50, y=75)
number2_entry = tk.Entry(window, width=36)
number2_entry.place(x=50, y=150)
answer_entry = tk.Entry(window, width=36)
answer_entry.place(x=50, y=300)

number1 = tk.Label(window, text='Введите первое число: ')
number1.place(x=50, y=50)
number2 = tk.Label(window, text='Введите второе число: ')
number2.place(x=50, y=125)
answer = tk.Label(window, text='Ответ: ')
answer.place(x=50, y=270)

window.mainloop()