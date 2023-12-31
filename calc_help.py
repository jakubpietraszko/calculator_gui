from help import is_float
from help import op_high, op_mid, op_low
from help import op_all, op_par
from help import operator_cast
from typing import List, AnyStr


class Str_to_List_of_Str():
    def __init__(self, arg: AnyStr) -> None:
        self.ret: List[AnyStr] = []
        list_op: List[AnyStr] = op_all + op_par

        temp: AnyStr = ''

        ret: List[AnyStr] = []

        for c in arg:
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

        ret2: List[AnyStr] = []
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

    def result(self) -> List[AnyStr]:
        return self.ret


class List_of_Str_to_RPN():
    def __init__(self, arg: List[AnyStr]) -> None:
        self.stack: List[AnyStr] = []
        self.queue: List[AnyStr] = []

        for e in arg:
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

    def result(self) -> List[AnyStr]:
        return self.queue


class RPN_to_Str():
    def __init__(self, arg: List[AnyStr]) -> None:
        self.stack: List[AnyStr] = []

        for e in arg:
            if is_float(e):
                self.stack.append(float(e))
                continue

            second: float = self.stack.pop()
            first: float = self.stack.pop()
            self.stack.append(operator_cast[e](first, second))

    def result(self) -> AnyStr:
        return str(self.stack[-1])
