import tkinter as tk
from functools import partial
from tkinter import messagebox  # 코드 잘못됐을 때 에러창 띄우려고
from train_win import LearnWinner


def check(app, lang, ntr_code, ntr_name, ntr_type, ntr_rate, ntr_msg, event):
    ntr_name.delete(0, 'end')
    ntr_type.delete(0, 'end')
    ntr_rate.delete(0, 'end')
    ntr_msg.delete(0, 'end')
    code = ntr_code.get()
    if code.isdigit() and (int(code) < 1 or int(code) > 800):
        if lang == 'eng':
            message = 'Code must be a countable number from 1 to 800.'
        elif lang == 'kr':
            message = '코드는 1부터 800까지의 숫자입니다.'
        else:
            message = '1から800までの数字を入力してください。'
        messagebox.showerror('ERROR', message)
        return
    lrn = LearnWinner(code, lang)
    name, type, rate, msg = lrn.train_winner()
    ntr_name.insert(0, 'NAME: ' + name)
    ntr_type.insert(0, 'TYPE: ' + type)
    ntr_rate.insert(0, 'WIN RATE: ' + ('%.2f' % rate) + '%')
    ntr_msg.insert(0, msg)


def mode_eng(app, event):
    new_win = tk.Toplevel(app)
    new_win.title('ENGLISH')
    new_win.geometry('450x280+450+250')
    new_win.resizable(False, False)
    lbl_code = tk.Label(new_win, text='\nEnter a name or a number code(1~800):', font=80)
    lbl_code.pack(anchor='w')
    ntr_code = tk.Entry(new_win, width=60)
    ntr_code.pack(fill='x', padx=5, expand=True)
    btn_ok = tk.Button(new_win, width=10, font=80, text='OK')
    btn_ok.pack()
    ntr_name = tk.Entry(new_win, width=60)
    ntr_name.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_type = tk.Entry(new_win, width=60)
    ntr_type.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_rate = tk.Entry(new_win, width=60)
    ntr_rate.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_msg = tk.Entry(new_win, width=60)
    ntr_msg.pack(fill='x', padx=5, ipady=10, expand=True)
    btn_ok.bind('<ButtonRelease-1>', partial(check, new_win, 'eng', ntr_code, ntr_name, ntr_type, ntr_rate, ntr_msg))


def mode_kr(app, event):
    new_win = tk.Toplevel(app)
    new_win.title('한국어')
    new_win.geometry('450x280+450+250')
    new_win.resizable(False, False)
    lbl_code = tk.Label(new_win, text='\n이름 또는 숫자 코드(1~800)를 입력하세요:', font=80)
    lbl_code.pack(anchor='w')
    ntr_code = tk.Entry(new_win, width=60)
    ntr_code.pack(fill='x', padx=5, expand=True)
    btn_ok = tk.Button(new_win, width=10, font=80, text='OK')
    btn_ok.pack()
    ntr_name = tk.Entry(new_win, width=60)
    ntr_name.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_type = tk.Entry(new_win, width=60)
    ntr_type.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_rate = tk.Entry(new_win, width=60)
    ntr_rate.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_msg = tk.Entry(new_win, width=60)
    ntr_msg.pack(fill='x', padx=5, ipady=10, expand=True)
    btn_ok.bind('<ButtonRelease-1>', partial(check, new_win, 'kr', ntr_code, ntr_name, ntr_type, ntr_rate, ntr_msg))


def mode_jp(app, event):
    new_win = tk.Toplevel(app)
    new_win.title('日本語')
    new_win.geometry('600x280+450+250')
    new_win.resizable(False, False)
    lbl_code = tk.Label(new_win, text='\nポケモンの名前または番号コード(1~800)を入力してください:', font=80)
    lbl_code.pack(anchor='w')
    ntr_code = tk.Entry(new_win, width=60)
    ntr_code.pack(fill='x', padx=5, expand=True)
    btn_ok = tk.Button(new_win, width=10, font=80, text='OK')
    btn_ok.pack()
    ntr_name = tk.Entry(new_win, width=60)
    ntr_name.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_type = tk.Entry(new_win, width=60)
    ntr_type.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_rate = tk.Entry(new_win, width=60)
    ntr_rate.pack(fill='x', padx=5, ipady=10, expand=True)
    ntr_msg = tk.Entry(new_win, width=60)
    ntr_msg.pack(fill='x', padx=5, ipady=10, expand=True)
    btn_ok.bind('<ButtonRelease-1>', partial(check, new_win, 'jp', ntr_code, ntr_name, ntr_type, ntr_rate, ntr_msg))


def make(app):
    # 언어 선택
    app.lbl_lang = tk.Label(app.sub_fr, font=80, text='\n\nChoose your language.')
    app.lbl_lang.pack()
    app.btn_eng = tk.Button(app.sub_fr, width=10, font=80, text='ENGLISH')
    app.btn_eng.pack(side='left', anchor='s', pady=5)
    app.btn_eng.bind('<Button-1>', partial(mode_eng, app))
    app.btn_kr = tk.Button(app.sub_fr, width=10, font=80, text='한국어')
    app.btn_kr.pack(side='left', anchor='s', pady=5)
    app.btn_kr.bind('<Button-1>', partial(mode_kr, app))
    app.btn_jp = tk.Button(app.sub_fr, width=10, font=80, text='日本語')
    app.btn_jp.pack(side='left', anchor='s', pady=5)
    app.btn_jp.bind('<Button-1>', partial(mode_jp, app))
