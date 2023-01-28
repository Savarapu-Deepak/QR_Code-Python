# Calculator Using Tkinter...

from tkinter import *

window = Tk()
window.title("CALCULATOR")
# Display Box
db = Entry(window, width=14, font=('Arial', 28), justify=RIGHT,bg='black',fg='orange',relief=RAISED)
db.grid(row=0, column=0, padx=10, pady=10, columnspan=3)


def clear():
    db.delete(0, END)


def btn_click(num): # To get Numbers side by side.
    cur_num = db.get()
    clear()
    f_num = cur_num + num
    db.insert(0, f_num)


first_num = 0
math = ''


def calc(math_type):
    global first_num, math
    math = math_type
    first_num = db.get()
    clear()


def equal():
    global first_num
    second_num = db.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        result = int(first_num) / int(second_num)
        result = round(result, 5)
    else:
        result = int(first_num) - int(second_num)
    db.insert(0, str(result))


# Buttons....
btn_0 = Button(window, text='0', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('0'),bg='black',fg='orange')

btn_1 = Button(window, text='1', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('1'),bg='black',fg='orange')
btn_2 = Button(window, text='2', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('2'),bg='black',fg='orange')
btn_3 = Button(window, text='3', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('3'),bg='black',fg='orange')

btn_4 = Button(window, text='4', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('4'),bg='black',fg='orange')
btn_5 = Button(window, text='5', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('5'),bg='black',fg='orange')
btn_6 = Button(window, text='6', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('6'),bg='black',fg='orange')

btn_7 = Button(window, text='7', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('7'),bg='black',fg='orange')
btn_8 = Button(window, text='8', font=('arial', 14), padx=36, pady=10, command=lambda: btn_click('8'),bg='black',fg='orange')
btn_9 = Button(window, text='9', font=('Arial', 14), padx=36, pady=10, command=lambda: btn_click('9'),bg='black',fg='orange')
# Clear Button
btn_clear = Button(window, text='clear', padx=74, pady=10, font=('arial', 14), command=clear,bg='black',fg='orange')
btn_div = Button(window, text='/', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('div'),bg='black',fg='orange')
btn_mul = Button(window, text='*', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('mul'),bg='black',fg='orange')

btn_sub = Button(window, text='-', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('sub'),bg='black',fg='orange')
btn_add = Button(window, text='+', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('add'),bg='black',fg='orange')

btn_equal = Button(window, text='=', padx=36, pady=40, font=('arial', 14), command=equal,bg='black',fg='orange')
# Grid System for Buttons
btn_div.grid(row=5, column=0, padx=2, pady=2)
btn_mul.grid(row=5, column=1, padx=2, pady=2)
btn_equal.grid(row=5, column=2, padx=2, pady=2, rowspan=2)

btn_sub.grid(row=6, column=0, padx=2, pady=2)
btn_add.grid(row=6, column=1, padx=2, pady=2)

btn_0.grid(row=4, column=0, padx=2, pady=2)
btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)
window.mainloop()
