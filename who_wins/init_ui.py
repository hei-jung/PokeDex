import tkinter as tk


class AppWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Pokemon Win Rate')
        self.master.geometry('450x280+400+200')
        self.master.resizable(True, True)
        self.sub_fr = None
        self.create_widgets()

    def create_widgets(self):
        self.sub_fr = tk.Label(self.master)
        self.sub_fr.pack()
