from help import is_float
from help import op_high, op_mid, op_low
from help import op_all
from help import operator_cast


class To_RPN():
    def __init__(self, data: list[str]) -> None:
        self.stack: list[str] = []
        self.queue: list[str] = []
        for e in data:
            if is_float(e):
                self.queue.append(e)
                continue

            if e in op_low:
                while len(self.stack) > 0 and self.stack[-1] in (op_low + op_mid):
                    self.queue.append(self.stack.pop())
                self.stack.append(e)
                continue

            if e in op_mid:
                while len(self.stack) > 0 and (self.stack[-1] in op_mid):
                    self.queue.append(self.stack.pop())
                self.stack.append(e)
                continue

            if e in op_high:
                self.stack.append(e)
                continue

            if e == '(':
                self.stack.append(e)
                continue

            if e == ')':
                while len(self.stack) > 0 and self.stack[-1] in op_all:
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
        return self.queue


class From_RPN_to_val():
    def __init__(self, data: list[str]) -> None:
        self.stack: list[float] = []

        for e in data:
            if is_float(e):
                self.stack.append(float(e))
                continue
            if e in op_all:
                second: float = self.stack.pop()
                first: float = self.stack.pop()
                self.stack.append(operator_cast[e](first, second))
                continue
                
    def result(self) -> str:
        return str(self.stack[-1])
