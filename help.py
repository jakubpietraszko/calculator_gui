from typing import Dict, Callable

op_high = ['^']
op_mid = ['*', '/']
op_low = ['+', '-']
op_all = op_low + op_mid + op_high


operator_cast: Dict[str, Callable[[float, float], float]] = \
                            {'+': lambda x, y: x + y,
                             '-': lambda x, y: x - y,
                             '*': lambda x, y: x * y,
                             '/': lambda x, y: x / y,
                             '^': lambda x, y: x ** y,
                             }


def is_float(arg: str) -> bool:
    try:
        float(arg)
        return True
    except ValueError:
        return False
