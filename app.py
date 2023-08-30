import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self) -> None:
        self.returned: bool = False

        self.root: tk.Tk = tk.Tk()
        self.root.title('Calculator')
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.main_frame: ttk.Frame = ttk.Frame(self.root)
        self.main_frame.grid(sticky="NWES",
                             padx=10,
                             pady=10)
        self.main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

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
        self.data_to_count_temp: str = ''
        self.data_to_count: tk.StringVar = tk.StringVar()
        self.data_to_count.set(self.data_to_count_temp)
        self.label: ttk.Label = ttk.Label(self.main_frame,
                                          textvariable=self.data_to_count)
        self.label.grid(column=0,
                        row=0,
                        columnspan=4,
                        sticky="NWES",
                        padx=(0, 0),
                        pady=(0, 3)
                        )

        for child in self.main_frame.winfo_children():
            child.grid(sticky="NWES",
                       padx=(0, 3),
                       pady=(0, 3))

        self.root.mainloop()

    def zero(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '0'
        self.data_to_count.set(self.data_to_count_temp)

    def one(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '1'
        self.data_to_count.set(self.data_to_count_temp)

    def two(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '2'
        self.data_to_count.set(self.data_to_count_temp)

    def three(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '3'
        self.data_to_count.set(self.data_to_count_temp)

    def four(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '4'
        self.data_to_count.set(self.data_to_count_temp)

    def five(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '5'
        self.data_to_count.set(self.data_to_count_temp)

    def six(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '6'
        self.data_to_count.set(self.data_to_count_temp)

    def seven(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '7'
        self.data_to_count.set(self.data_to_count_temp)

    def eight(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '8'
        self.data_to_count.set(self.data_to_count_temp)

    def nine(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '9'
        self.data_to_count.set(self.data_to_count_temp)

    def c(self) -> None:
        self.data_to_count_temp = ''
        self.data_to_count.set('')

    def eq(self) -> None:
        self.calculate()

    def plus(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '+'
        self.data_to_count.set(self.data_to_count_temp)

    def minus(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '-'
        self.data_to_count.set(self.data_to_count_temp)

    def mult(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '*'
        self.data_to_count.set(self.data_to_count_temp)

    def dev(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '/'
        self.data_to_count.set(self.data_to_count_temp)

    def calculate(self) -> None:
        self.data_to_count_temp = self.count()
        self.data_to_count.set(self.data_to_count_temp)
        self.returned = True

    def count(self) -> float:
        print(self.data_to_count_temp)
        return 10
