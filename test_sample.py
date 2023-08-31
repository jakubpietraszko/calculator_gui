from to_rpn import To_RPN, From_RPN_to_val
from pytest import approx

def dif(x1: float, x2: float) -> bool:
    return abs(x1 - x2) < 0.01


def test1() -> None:
    input: list[str] = ['(', '2', '+', '3', ')', '*', '5']
    expected_output: list[str] = ['2', '3', '+', '5', '*']
    output: list[str] = To_RPN(input).result()
    assert expected_output == output


def test_2() -> None:
    input: list[str] = ['12', '+', '2', '*', '(', '3', '*', '4', '+', '10', '/', '5', ')']
    expected_output: list[str] = ['12', '2', '3',  '4', '*', '10', '5', '/', '+', '*', '+']
    output: list[str] = To_RPN(input).result()
    assert expected_output == output


def test3() -> None:
    input: list[str] = ['5', '+', '(', '1', '+', '2', ')', '*', '4', '-', '3']
    expected_output: list[str] = ['5', '1', '2', '+', '4', '*', '+', '3', '-']
    output: list[str] = To_RPN(input).result()
    assert expected_output == output


def test4() -> None:
    input: list[str] = ['3', '+', '4','*', '2', '/', '(', '1', '-', '5', ')', '^', '2']
    expected_output: list[str] = ['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+']
    output: list[str] = To_RPN(input).result()
    assert expected_output == output


def test5() -> None:
    input: list[str] = ['12', '2', '3',  '4', '*', '10', '5', '/', '+', '*', '+']
    expected_output: float = 40.0
    output: float = float(From_RPN_to_val(input).result())
    assert expected_output == approx(output)


def test6() -> None:
    input: list[str] = ['5', '1', '2', '+', '4', '*', '+', '3', '-']
    expected_output: float = 14.0
    output: float = float(From_RPN_to_val(input).result())
    assert expected_output == approx(output)
