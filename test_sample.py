from to_rpn import Str_to_List_of_Str, List_of_Str_to_RPN, RPN_to_Str
from pytest import approx
from typing import AnyStr, List


def test_Str_to_List_of_Str_1() -> None:
    input: str = '(3+5)*(7-2)'
    expected_output: list[str] = ['(', '3.0', '+', '5.0', ')',
                                  '*', '(', '7.0', '-', '2.0', ')']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_Str_to_List_of_Str_2() -> None:
    input: str = '(2+3)*5'
    expected_output: list[str] = ['(', '2.0', '+',
                                  '3.0', ')', '*', '5.0']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_Str_to_List_of_Str_3() -> None:
    input: str = '12+2*(3*4+10/5)'
    expected_output: list[str] = ['12.0', '+', '2.0', '*', '(', '3.0', '*',
                                  '4.0', '+', '10.0', '/', '5.0', ')']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_Str_to_List_of_Str_4() -> None:
    input: str = '-5+(1+2)*4-3'
    expected_output: list[str] = ['-5.0', '+', '(', '1.0', '+',
                                  '2.0', ')', '*', '4.0', '-', '3.0']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_Str_to_List_of_Str_5() -> None:
    input: str = '3+4*2/(1-5)^2'
    expected_output: list[str] = ['3.0', '+', '4.0', '*', '2.0', '/', '(',
                                  '1.0', '-', '5.0', ')', '^', '2.0']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_Str_to_List_of_Str_6() -> None:
    input: str = '((5-3)*2)'
    expected_output: list[str] = ['(', '(', '5.0', '-',
                                  '3.0', ')', '*', '2.0', ')']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_Str_to_List_of_Str_7() -> None:
    input: str = '-0.1-(-0.2+2)'
    expected_output: list[str] = ['-0.1', '-', '(',
                                  '-0.2', '+', '2.0', ')']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_Str_to_List_of_Str_8() -> None:
    input: str = '-0.9+0.9+(2^(-3))'
    expected_output: list[str] = ['-0.9', '+', '0.9', '+', '(', '2.0',
                                  '^', '(', '-3.0', ')', ')']
    output: list[str] = Str_to_List_of_Str(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_1() -> None:
    input: List[AnyStr] = ['(', '2', '+', '3', ')', '*', '5']
    expected_output: List[AnyStr] = ['2', '3', '+', '5', '*']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_2() -> None:
    input: List[AnyStr] = ['12', '+', '2', '*', '(', '3', '*', '4',
                           '+', '10', '/', '5', ')']
    expected_output: List[AnyStr] = ['12', '2', '3',  '4', '*',
                                     '10', '5', '/', '+', '*', '+']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_3() -> None:
    input: List[AnyStr] = ['5', '+', '(', '1', '+', '2',
                           ')', '*', '4', '-', '3']
    expected_output: List[AnyStr] = ['5', '1', '2', '+',
                                     '4', '*', '+', '3', '-']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_4() -> None:
    input: List[AnyStr] = ['3', '+', '4', '*', '2', '/', '(',
                           '1', '-', '5', ')', '^', '2']
    expected_output: List[AnyStr] = ['3', '4', '2', '*', '1',
                                     '5', '-', '2', '^', '/', '+']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_5() -> None:
    input: List[AnyStr] = ['(', '3', '+', '4', ')', '*', '5']
    expected_output: List[AnyStr] = ['3', '4', '+', '5', '*']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_6() -> None:
    input: List[AnyStr] = ['2', '+', '4']
    expected_output: List[AnyStr] = ['2', '4', '+']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_7() -> None:
    input: List[AnyStr] = ['2', '*', '4', '+', '8']
    expected_output: List[AnyStr] = ['2', '4', '*', '8', '+']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_List_of_Str_to_RPN_8() -> None:
    input: List[AnyStr] = ['2', '*', '(', '4', '+', '8', ')']
    expected_output: List[AnyStr] = ['2', '4', '8', '+', '*']
    output: List[AnyStr] = List_of_Str_to_RPN(input).result()
    assert expected_output == output


def test_RPN_to_Str_1() -> None:
    input: List[AnyStr] = ['12', '2', '3',  '4', '*', '10',
                           '5', '/', '+', '*', '+']
    expected_output: float = 40.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)


def test_RPN_to_Str_2() -> None:
    input: List[AnyStr] = ['5', '1', '2', '+', '4',
                           '*', '+', '3', '-']
    expected_output: float = 14.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)


def test_RPN_to_Str_3() -> None:
    input: List[AnyStr] = ['2', '4', '*', '8', '+']
    expected_output: float = 16.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)


def test_RPN_to_Str_4() -> None:
    input: List[AnyStr] = ['2', '4', '8', '+', '*']
    expected_output: float = 24.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)


def test_RPN_to_Str_5() -> None:
    input: List[AnyStr] = ['3', '2', '*', '11', '-']
    expected_output: float = -5.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)


def test_RPN_to_Str_6() -> None:
    input: List[AnyStr] = ['2', '5', '*', '4', '+',
                           '3', '2', '*', '1', '+', '/']
    expected_output: float = 2.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)


def test_RPN_to_Str_7() -> None:
    input: List[AnyStr] = ['2', '1', '+', '3', '*']
    expected_output: float = 9.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)


def test_RPN_to_Str_8() -> None:
    input: List[AnyStr] = ['3', '5', '+',
                           '7', '2', '-', '*']
    expected_output: float = 40.0
    output: float = float(RPN_to_Str(input).result())
    assert expected_output == approx(output)
