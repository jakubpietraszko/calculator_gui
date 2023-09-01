import tkinter as tk
from tkinter import ttk
from to_rpn import Str_to_List_of_Str, List_of_Str_to_RPN, RPN_to_Str
from typing import List, AnyStr
from help import num_to_grid
from functools import partial


class App:
    def __init__(self) -> None:

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

        self.data_to_count_temp: str = ''

        self.data_to_count: tk.StringVar = tk.StringVar()
        self.data_to_count.set(self.data_to_count_temp)

        self.label: ttk.Label = ttk.Label(self.main_frame,
                                          textvariable=self.data_to_count)
        self.label.grid(column=0,
                        row=0,
                        columnspan=4,
                        )

        self.buttons: List[ttk.Button] = []
        for b in num_to_grid:
            button: ttk.Button = ttk.Button(self.main_frame,
                                            text=b,
                                            command=partial(self.btn_temp, b))

            button.grid(column=num_to_grid[b][0],
                        row=num_to_grid[b][1])
            self.buttons.append(button)

        self.button_c: ttk.Button = ttk.Button(self.main_frame,
                                               text='c',
                                               command=self.c)
        self.button_c.grid(column=4,
                           row=0,
                           )

        self.button_eq: ttk.Button = ttk.Button(self.main_frame,
                                                text='=',
                                                command=self.eq)
        self.button_eq.grid(column=2,
                            row=4,
                            )

        self.button_del: ttk.Button = ttk.Button(self.main_frame,
                                                 text='del',
                                                 command=self.delete)
        self.button_del.grid(column=4,
                             row=1,
                             )

        for child in self.main_frame.winfo_children():
            child.grid(sticky="NWES",
                       padx=(0, 3),
                       pady=(0, 3))

        self.root.mainloop()

    def btn_temp(self, val: AnyStr) -> None:
        self.data_to_count_temp += val
        self.data_to_count.set(self.data_to_count_temp)

    def c(self) -> None:
        self.data_to_count_temp = ''
        self.data_to_count.set('')

    def eq(self) -> None:
        if self.data_to_count_temp != '':
            self.calculate()

    def delete(self) -> None:
        if self.data_to_count_temp == '':
            pass
        else:
            self.data_to_count_temp = self.data_to_count_temp[:-1]
            self.data_to_count.set(self.data_to_count_temp)

    def calculate(self) -> None:

        ret1: List[AnyStr] = \
            Str_to_List_of_Str(self.data_to_count_temp).result()

        ret2: List[AnyStr] = List_of_Str_to_RPN(ret1).result()

        ret3: AnyStr = RPN_to_Str(ret2).result()

        self.data_to_count_temp = ret3
        self.data_to_count.set(self.data_to_count_temp)
