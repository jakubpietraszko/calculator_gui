import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title('Calculator')
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.main_frame: ttk.Frame = ttk.Frame(self.root,
                                               padding='3 3 3 3')
        self.main_frame.grid(sticky="NWES")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.button_0: ttk.Button = ttk.Button(self.main_frame,
                                               text='0',
                                               command=self.zero)
        self.button_0.grid(column=1,
                           row=4,
                           )

        self.button_1: ttk.Button = ttk.Button(self.main_frame,
                                               text='1',
                                               command=self.one)
        self.button_1.grid(column=0,
                           row=1,
                           )

        self.button_2: ttk.Button = ttk.Button(self.main_frame,
                                               text='2',
                                               command=self.two)
        self.button_2.grid(column=1,
                           row=1,
                           )

        self.button_3: ttk.Button = ttk.Button(self.main_frame,
                                               text='3',
                                               command=self.three)
        self.button_3.grid(column=2,
                           row=1,
                           )

        self.button_4: ttk.Button = ttk.Button(self.main_frame,
                                               text='4',
                                               command=self.four)
        self.button_4.grid(column=0,
                           row=2,
                           )

        self.button_5: ttk.Button = ttk.Button(self.main_frame,
                                               text='5',
                                               command=self.five)
        self.button_5.grid(column=1,
                           row=2,
                           )

        self.button_6: ttk.Button = ttk.Button(self.main_frame,
                                               text='6',
                                               command=self.six)
        self.button_6.grid(column=2,
                           row=2,
                           )

        self.button_7: ttk.Button = ttk.Button(self.main_frame,
                                               text='7',
                                               command=self.seven)
        self.button_7.grid(column=0,
                           row=3,
                           )

        self.button_8: ttk.Button = ttk.Button(self.main_frame,
                                               text='8',
                                               command=self.eight)
        self.button_8.grid(column=1,
                           row=3,
                           )

        self.button_9: ttk.Button = ttk.Button(self.main_frame,
                                               text='9',
                                               command=self.nine)
        self.button_9.grid(column=2,
                           row=3,
                           )

        self.button_c: ttk.Button = ttk.Button(self.main_frame,
                                               text='c',
                                               command=self.c)
        self.button_c.grid(column=0,
                           row=4,
                           )

        self.button_eq: ttk.Button = ttk.Button(self.main_frame,
                                                text='=',
                                                command=self.eq)
        self.button_eq.grid(column=2,
                            row=4,
                            )

        self.button_plus: ttk.Button = ttk.Button(self.main_frame,
                                                  text='+',
                                                  command=self.plus)
        self.button_plus.grid(column=3,
                              row=1,
                              )

        self.button_minus: ttk.Button = ttk.Button(self.main_frame,
                                                   text='-',
                                                   command=self.minus)
        self.button_minus.grid(column=3,
                               row=2,
                               )

        self.button_mult: ttk.Button = ttk.Button(self.main_frame,
                                                  text='*',
                                                  command=self.mult)
        self.button_mult.grid(column=3,
                              row=3,
                              )

        self.button_dev: ttk.Button = ttk.Button(self.main_frame,
                                                 text='/',
                                                 command=self.dev)
        self.button_dev.grid(column=3,
                             row=4,
                             )

        self.data_to_count: tk.StringVar = tk.StringVar()
        self.label: ttk.Label = ttk.Label(self.main_frame,
                                          textvariable=self.data_to_count)
        self.label.grid(column=0,
                        row=0,
                        columnspan=4,
                        rowspan=1,
                        )

        for child in self.main_frame.winfo_children():
            print(child)
            child.grid_configure(padx=3,
                                 pady=3)
            if child.winfo_ismapped() and child.grid_info():
                child.grid(sticky="NWES")
                col = child.grid_info()['column']
                row = child.grid_info()['row']

                self.main_frame.columnconfigure(col, weight=1)
                self.main_frame.rowconfigure(row, weight=1)

        self.root.mainloop()

    def zero(self) -> None:
        print(0)

    def one(self) -> None:
        print(1)

    def two(self) -> None:
        print(2)

    def three(self) -> None:
        print(3)

    def four(self) -> None:
        print(4)

    def five(self) -> None:
        print(5)

    def six(self) -> None:
        print(6)

    def seven(self) -> None:
        print(7)

    def eight(self) -> None:
        print(8)

    def nine(self) -> None:
        print(9)

    def c(self) -> None:
        print('c')

    def eq(self) -> None:
        print('=')

    def plus(self) -> None:
        print('+')

    def minus(self) -> None:
        print('-')

    def mult(self) -> None:
        print('*')

    def dev(self) -> None:
        print('/')
