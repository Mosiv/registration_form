from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

window = ThemedTk(theme='clearlooks')
window.title('Форма регистрации')
window.resizable(False, False)


def window_exit():
    answer = messagebox.askokcancel(title='Выход', message="Закрыть программу?")
    if answer:
        window.destroy()


def print_data():
    messagebox.showinfo("Зарегистрирован!", e_user.get() + " " + e_pass.get())
    login = e_user.get()
    passw = e_pass.get()
    print(login)
    print(passw)


l_user = ttk.Label(window, text='Login').grid(row=0, column=0, padx=10, pady=10, sticky=W)
e_user = ttk.Entry(window)
e_user.grid(row=0, column=1, columnspan=2, padx=10, sticky=W+E)

l_pass = ttk.Label(window, text='Password:').grid(row=1, column=0, padx=10, pady=10)
e_pass = ttk.Entry(window)
e_pass.grid(row=1, column=1, columnspan=2, padx=10, sticky=W+E)

btn_login = ttk.Button(window, text='Вход', command=print_data).grid(row=2, column=0, pady=10)
btn_reg = ttk.Button(window, text='Регистация', command=print_data).grid(row=2, column=1)
btn_forgot = ttk.Button(window, text='Забыли пароль').grid(row=2, column=2, padx=10)

btn_exit = ttk.Button(window, text='Выход', command=window_exit)
btn_exit.grid(row=2, column=3, padx=10)

window.mainloop()
