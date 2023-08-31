from help import is_float
from math import log, sin, cos, tan,sqrt


class To_RPN():
    def __init__(self, data: list[str]) -> None:
        self.stack: list[str] = []
        self.queue: list[str] = []
        print('data', data)
        for e in data:
            if is_float(e):
                self.queue.append(e)
                continue

            if e in ['^(', '√(', 'ln(', 'sin(', 'cos(', 'tan(', '-√(', '-ln(', '-sin(', '-cos(', '-tan(']:
                print(e)
                self.stack.append(e)
                continue

            if e in ['+', '-']:
                while len(self.stack) > 0 and (self.stack[-1] in ['+', '-']):
                    self.queue.append(self.stack.pop())
                self.stack.append(e)
                continue
            if e in ['*', '/']:
                while len(self.stack) > 0 and (self.stack[-1] in ['*', '/']):
                    self.queue.append(self.stack.pop())
                self.stack.append(e)
                continue
            if e == '^':
                self.stack.append(e)
                continue

            if e == '(':
                self.stack.append(e)
                continue

            if e == ')':
                while len(self.stack) > 0 and self.stack[-1] in ['+', '-', '*', '/', '^']:
                    self.queue.append(self.stack.pop())
                if len(self.stack) > 0:
                    if self.stack[-1] == '(':
                        self.stack.pop()
                        continue
                    else:
                        self.queue.append(self.stack[-1][:-1])
                        self.stack.pop()
                else:
                    continue
        while len(self.stack) > 0:
            self.queue.append(self.stack.pop())

    def result(self) -> list[str]:
        print(self.queue)
        return self.queue


class From_RPN_to_val():
    def __init__(self, data: list[str]) -> None:
        self.ret: float = 0
        self.stack: list[float] = []

        for e in data:
            if is_float(e):
                self.stack.append(float(e))
                continue
            if e in ['+', '-', '*', '/', '^']:
                second: float = self.stack.pop()
                first: float = self.stack.pop()
                if e == '+':
                    self.stack.append(first + second)
                    continue
                if e == '-':
                    self.stack.append(first - second)
                    continue
                if e == '*':
                    self.stack.append(first * second)
                    continue
                if e == '/':
                    self.stack.append(first / second)
                    continue
                if e == '^':
                    self.stack.append(first ** second)
                    continue
            if e in ['ln', 'sin', 'cos', 'tan', '√']:
                last: float = self.stack.pop()
                if e == 'ln':
                    self.stack.append(log(last))
                    continue
                if e == 'sin':
                    self.stack.append(sin(last))
                    continue
                if e == 'cos':
                    self.stack.append(cos(last))
                    continue
                if e == 'tan':
                    self.stack.append(tan(last))
                    continue
                if e == '√':
                    self.stack.append(sqrt(last))
                    continue
            if e in ['-ln', '-sin', '-cos', '-tan', '-√']:
                last: float = self.stack.pop()
                if e == '-ln':
                    self.stack.append(-log(last))
                    continue
                if e == '-sin':
                    self.stack.append(-sin(last))
                    continue
                if e == '-cos':
                    self.stack.append(-cos(last))
                    continue
                if e == '-tan':
                    self.stack.append(-tan(last))
                    continue
                if e == '-√':
                    self.stack.append(-sqrt(last))
                    continue
                    
        self.val = self.stack[-1]

    def result(self) -> str:
        return str(self.val)


if __name__ == '__main__':
    data: list[str] = ['3', '+', '4', '*', '2', '/',
                       '(', '1', '-', '5', ')', '^', '2']
    print('before', data)
    temp: To_RPN = To_RPN(data)
    print('after', temp.result())