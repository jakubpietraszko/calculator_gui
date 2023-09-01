from help import is_float
from help import op_high, op_mid, op_low
from help import op_all, op_par
from help import operator_cast


class Str_to_List_of_Str():
    def __init__(self, data: str) -> None:
        self.ret: list[str] = []
        list_op: list[str] = op_all + op_par

        temp: str = ''

        ret: list[str] = []
        for c in data:
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
        for i in range(len(ret)):
            if i == 0 and ret[0] == '-' and len(ret) > 1 and is_float(ret[1]):
                e = float(ret[1])
                if e > 0:
                    ret2.append(str(-e))
                    i += 1
                    check = True
                    continue
            if i != 0 and ret[i] == '-' and \
                                    len(ret) >= i + 2 and \
                                    ret[i - 1] == '(' and is_float(ret[i + 1]):
                e = float(ret[i + 1])
                if e > 0:
                    ret2.append(str(-e))
                    i += 1
                    check = True
                    continue
            if check is True:
                check = False
                continue
            if is_float(ret[i]):
                ret2.append(str(float(ret[i])))
                continue
            ret2.append(str(ret[i]))
            self.ret = ret2

    def result(self) -> list[str]:
        return self.ret


class List_of_Str_to_RPN():
    def __init__(self, data: list[str]) -> None:
        self.stack: list[str] = []
        self.queue: list[str] = []
        for e in data:
            if is_float(e):
                self.queue.append(e)
                continue

            if e in op_low:
                while len(self.stack) > 0 and \
                        self.stack[-1] in (op_low + op_mid):

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


class RPN_to_Str():
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
