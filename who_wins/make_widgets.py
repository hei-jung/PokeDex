import tkinter as tk
from functools import partial
from tkinter import messagebox  # 코드 잘못됐을 때 에러창 띄우려고
from train_win import LearnWinner


def check(app, event):
    app.ntr_name.delete(0, 'end')
    app.ntr_type.delete(0, 'end')
    app.ntr_rate.delete(0, 'end')
    app.ntr_msg.delete(0, 'end')
    code = app.ntr_code.get()
    if code.isdigit() and (int(code) < 1 or int(code) > 800):
        messagebox.showerror('ERROR', '코드는 1부터 800까지의 숫자입니다.')
        return
    lrn = LearnWinner(code)
    name, type, rate, msg = lrn.train_winner()
    app.ntr_name.insert(0, '이름: ' + name)
    app.ntr_type.insert(0, '속성: ' + type)
    app.ntr_rate.insert(0, '승률: ' + ('%.2f' % rate) + '%')
    app.ntr_msg.insert(0, msg)


def make(app):
    app.lbl_code = tk.Label(app.sub_fr, text='\n포켓몬 이름 또는 코드(1~800):', font=80)
    app.lbl_code.pack(anchor='w')
    app.ntr_code = tk.Entry(app.sub_fr, width=60)
    app.ntr_code.pack(fill='x', padx=5, expand=True)
    app.btn_ok = tk.Button(app.sub_fr, width=10, font=80, text='확인')
    app.btn_ok.pack()
    app.btn_ok.bind('<ButtonRelease-1>', partial(check, app))
    app.ntr_name = tk.Entry(app.sub_fr, width=60)
    app.ntr_name.pack(fill='x', padx=5, ipady=10, expand=True)
    app.ntr_type = tk.Entry(app.sub_fr, width=60)
    app.ntr_type.pack(fill='x', padx=5, ipady=10, expand=True)
    app.ntr_rate = tk.Entry(app.sub_fr, width=60)
    app.ntr_rate.pack(fill='x', padx=5, ipady=10, expand=True)
    app.ntr_msg = tk.Entry(app.sub_fr, width=60)
    app.ntr_msg.pack(fill='x', padx=5, ipady=10, expand=True)
