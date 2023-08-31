import tkinter as tk
from tkinter import ttk
from help import is_float
from to_rpn import To_RPN, From_RPN_to_val


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
        self.button_0.grid(column=0,
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
        self.button_c.grid(column=4,
                           row=0,
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

        #self.button_sqrt: ttk.Button = ttk.Button(self.main_frame,
        #                                          text='√',
        #                                          command=self.sqrt)
        #self.button_sqrt.grid(column=4,
        #                      row=1,
        #                      )

        #self.button_ln: ttk.Button = ttk.Button(self.main_frame,
        #                                        text='ln',
        #                                        command=self.ln)
        #self.button_ln.grid(column=4,
        #                    row=2,
        #                    )

        #self.button_sin: ttk.Button = ttk.Button(self.main_frame,
        #                                         text='sin',
        #                                         command=self.sin)
        #self.button_sin.grid(column=5,
        #                     row=2,
        #                     )

        #self.button_cos: ttk.Button = ttk.Button(self.main_frame,
        #                                         text='cos',
        #                                         command=self.cos)
        #self.button_cos.grid(column=5,
        #                     row=3,
        #                     )

        #self.button_tan: ttk.Button = ttk.Button(self.main_frame,
        #                                         text='tan',
        #                                         command=self.tan)
        #self.button_tan.grid(column=5,
        #                     row=4,
        #                     )

        self.button_left_par: ttk.Button = ttk.Button(self.main_frame,
                                                      text='(',
                                                      command=self.left_par)
        self.button_left_par.grid(column=4,
                                  row=3,
                                  )

        self.button_right_par: ttk.Button = ttk.Button(self.main_frame,
                                                       text=')',
                                                       command=self.right_par)
        self.button_right_par.grid(column=4,
                                   row=4,
                                   )

        self.button_dot: ttk.Button = ttk.Button(self.main_frame,
                                                 text='.',
                                                 command=self.dot)
        self.button_dot.grid(column=1,
                             row=4,
                             )

        self.button_del: ttk.Button = ttk.Button(self.main_frame,
                                                 text='del',
                                                 command=self.delete)
        self.button_del.grid(column=4,
                             row=1,
                             )
        self.button_pow: ttk.Button = ttk.Button(self.main_frame,
                                                 text='^',
                                                 command=self.pow)
        self.button_pow.grid(column=4,
                             row=2,
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
        #if self.returned is True:
        #    self.returned = False
        #    self.data_to_count_temp = ''
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
        if self.data_to_count_temp != '':
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

    def sqrt(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '√('
        self.data_to_count.set(self.data_to_count_temp)

    def dot(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '.'
        self.data_to_count.set(self.data_to_count_temp)

    def ln(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += 'ln('
        self.data_to_count.set(self.data_to_count_temp)

    def sin(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += 'sin('
        self.data_to_count.set(self.data_to_count_temp)

    def cos(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += 'cos('
        self.data_to_count.set(self.data_to_count_temp)

    def tan(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += 'tan('
        self.data_to_count.set(self.data_to_count_temp)

    def left_par(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '('
        self.data_to_count.set(self.data_to_count_temp)

    def right_par(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += ')'
        self.data_to_count.set(self.data_to_count_temp)

    def delete(self) -> None:
        if self.data_to_count_temp == '':
            pass
        else:
            self.data_to_count_temp = self.data_to_count_temp[:-1]
            self.data_to_count.set(self.data_to_count_temp)

    def pow(self) -> None:
        if self.returned is True:
            self.returned = False
            self.data_to_count_temp = ''
        self.data_to_count_temp += '^'
        self.data_to_count.set(self.data_to_count_temp)

    def calculate(self) -> None:

        list_op: list[str] = ['*',
                              '/',
                              '+',
                              '-',
                              '√',
                              '(',
                              ')',
                              '^',
                              ]
        temp: str = ''
        ret: list[str] = []
        for c in self.data_to_count_temp:
            if c not in list_op:
                temp += c
            else:
                if temp != '':
                    ret.append(temp)
                temp = ''
                if ret != '':
                    ret.append(c)
        if temp != '':
            ret.append(temp)

        ret2: list[str] = []
        check: bool = False
        print('ret', ret)
        for i in range(len(ret)):
            if i == 0 and ret[0] == '-' and len(ret) > 1 and is_float(ret[1]):
                e = float(ret[1])
                if e > 0:
                    ret2.append(-e)
                    i += 1
                    check = True
                    continue
            if i == 0 and ret[0] == '-' and len(ret) > 1 and ret[1] in ['sin', 'ln', 'cos', 'tan', '√']:
                ret2.append(-1)
                ret2.append('*')
                continue

            if i != 0 and ret[i] == '-' and len(ret) >= i + 2 and ret[i - 1] == '(' and is_float(ret[i + 1]):
                e = float(ret[i + 1])
                if e > 0:
                    ret2.append(-e)
                    i += 1
                    check = True
                    continue
            if i != 0 and ret[i] == '-' and len(ret) >= i + 2 and  ret[i + 1] in ['sin', 'ln', 'cos', 'tan', '√', '-sin', '-ln', '-cos', '-tan', '-√']:
                ret2.append('-' + ret[i + 1])
                check = True
                continue
            if check is True:
                check = False
                continue
            if is_float(ret[i]):
                ret2.append(float(ret[i]))
                continue
            ret2.append(ret[i])
        print('ret2', ret2)
        ret3: list[str] = []
        check: bool = False
        for i in range(len(ret2)):
            if check is True:
                check = False
                continue
            if ret2[i] in ['sin', 'cos', 'tan', 'ln', '√', '^(', '-sin', '-cos', '-tan', '-ln', '-√'] and ret2[i + 1] == '(':
                ret3.append(ret2[i] + '(')
                check = True
                continue
            ret3.append(ret2[i])
        print('ret3', ret3)
        ret4: list[str] = [str(e) for e in ret3]
        print('ret4', ret4)

        temp: To_RPN = To_RPN(ret4)

        temp = temp.result()
        print('ret5', temp)
        temp2: From_RPN_to_val = From_RPN_to_val(temp)

        self.data_to_count_temp = temp2.result()
        print('ret6', self.data_to_count_temp)
        self.data_to_count.set(self.data_to_count_temp)

        self.returned = True
