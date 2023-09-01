from typing import AnyStr, List, Dict, Tuple, Callable

op_high: List[AnyStr] = ['^']
op_mid: List[AnyStr] = ['*', '/']
op_low: List[AnyStr] = ['+', '-']
op_par: List[AnyStr] = ['(', ')']
op_all: List[AnyStr] = op_low + op_mid + op_high


operator_cast: Dict[str, Callable[[float, float], float]] = \
                            {'+': lambda x, y: x + y,
                             '-': lambda x, y: x - y,
                             '*': lambda x, y: x * y,
                             '/': lambda x, y: x / y,
                             '^': lambda x, y: x ** y,
                             }


num_to_grid: Dict['str', Tuple[int, int]] = \
                    {
                        '0': (0, 4),
                        '1': (0, 1),
                        '2': (1, 1),
                        '3': (2, 1),
                        '4': (0, 2),
                        '5': (1, 2),
                        '6': (2, 2),
                        '7': (0, 3),
                        '8': (1, 3),
                        '9': (2, 3),
                        '+': (3, 1),
                        '-': (3, 2),
                        '*': (3, 3),
                        '/': (3, 4),
                        '^': (4, 2),
                        '(': (4, 3),
                        ')': (4, 4),
                        '.': (1, 4),
                    }


def is_float(arg: AnyStr) -> bool:
    try:
        float(arg)
        return True
    except ValueError:
        return False
